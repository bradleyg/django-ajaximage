#-*- coding: utf-8 -*-
from django.core.files.storage import default_storage
from django.db.models.fields.files import FileDescriptor, FieldFile
from django.db.models import Field
from django.conf import settings
from .widgets import AjaxImageWidget


class AjaxImageField(Field):

    storage = default_storage
    attr_class = FieldFile
    descriptor_class = FileDescriptor

    def __init__(self, *args, **kwargs):
        upload_to = kwargs.pop('upload_to', '')
        max_height = kwargs.pop('max_height', 0)
        max_width = kwargs.pop('max_width', 0)
        crop = kwargs.pop('crop', False)
        crop = 1 if crop is True else 0

        if crop is 1 and (max_height is 0 or max_width is 0):
            raise Exception('Both max_width and max_height are needed if cropping')

        self.widget = AjaxImageWidget(
            upload_to=upload_to,
            max_width=max_width,
            max_height=max_height,
            crop=crop
        )
        super(AjaxImageField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(AjaxImageField, self).contribute_to_class(cls, name, virtual_only)
        setattr(cls, self.name, self.descriptor_class(self))

    def get_prep_value(self, value):
        """Returns field's value prepared for saving into a database."""
        # Need to convert File objects provided via a form to unicode for database insertion
        if value is None:
            return None
        return str(value)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(AjaxImageField, self).formfield(**defaults)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^ajaximage\.fields\.AjaxImageField"])