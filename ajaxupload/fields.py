#-*- coding: utf-8 -*-
from django.db.models import Field
from django.forms import widgets
from ajaxupload.widgets import AjaxUploadEditor


class AjaxUploadField(Field):
    def __init__(self, *args, **kwargs):
        upload_to = kwargs.pop('upload_to', '')
        self.widget = AjaxUploadEditor(upload_to=upload_to)
        super(AjaxUploadField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(AjaxUploadField, self).formfield(**defaults)
