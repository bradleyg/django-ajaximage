from django.shortcuts import render
from django.views.generic import FormView

from .forms import AjaxImageUploadForm


class MyView(FormView):
    template_name = 'form.html'
    form_class = AjaxImageUploadForm