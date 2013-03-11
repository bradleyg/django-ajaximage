#-*- coding: utf-8 -*-
from django.db.models import Field
from django.forms import widgets
from ajaxupload.widgets import AjaxEditor


class AjaxField(Field):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('ajax_options', {})
        upload_to = kwargs.pop('upload_to', '')
        self.widget = AjaxEditor(ajax_options=options, upload_to=upload_to)
        super(AjaxField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(AjaxField, self).formfield(**defaults)
