import os
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf import settings

PREPEND_MEDIA_URL = getattr(settings, 'AJAXIMAGE_PREPEND_MEDIA_URL', True)

HTML = """
<div class="ajaximage" data-url="{upload_url}">
    <a class="link" target="_blank" href="{file_url}"><img src="{file_url}"></a>
    <a class="remove" href="#remove">Remove</a>
    <input type="hidden" value="{file_path}" id="{element_id}" name="{name}" />
    <input type="file" class="fileinput" />
    <div class="progress progress-striped active">
        <div class="bar"></div>
    </div>
</div>
"""


class AjaxImageEditor(widgets.TextInput):

    class Media:
        js = (
            'shared-bg/js/jquery-1.10.0.min.js',
            'shared-bg/js/jquery.iframe-transport.js',
            'shared-bg/js/jquery.ui.widget.js',
            'shared-bg/js/jquery.fileupload.js',
            'ajaximage/js/ajaximage.js',
        )
        css = {
            'all': (
                'shared-bg/css/bootstrap-progress.min.css',
                'ajaximage/css/styles.css',
            )
        }

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        self.max_width = kwargs.pop('max_width', '')
        self.max_height = kwargs.pop('max_height', '')
        self.crop = kwargs.pop('crop', '')
        super(AjaxImageEditor, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        element_id = final_attrs.get('id')
        
        kwargs = {'upload_to': self.upload_to,
                  'max_width': self.max_width,
                  'max_height': self.max_height,
                  'crop': self.crop}
        
        upload_url = reverse('ajaximage', kwargs=kwargs)
        file_path = value if value else ''
        if PREPEND_MEDIA_URL is False and len(file_path) > 0:
            file_url = os.path.join(settings.MEDIA_URL, file_path)
        else:
            file_url = file_path

        file_name = os.path.basename(file_url)
        
        output = HTML.format(upload_url=upload_url,
                             file_url=file_url,
                             file_name=file_name,
                             file_path=file_path,
                             element_id=element_id,
                             name=name)
        
        return mark_safe(unicode(output))
