from django import forms

from ajaximage.widgets import AjaxImageWidget


class AjaxImageUploadForm(forms.Form):
    images = forms.FileField(widget=AjaxImageWidget())