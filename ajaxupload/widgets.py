from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf import settings


HTML = """
<div class="ajaxupload" data-url="%s">
    <img src="%s">
    <a class="link" href="%s" target="_blank">%s</a>
    <a class="remove" href="#remove">Remove</a>
    <input type="hidden" value="%s" id="%s" name="%s" />
    <input type="file" class="fileinput" />
    <div class="progress progress-striped active">
        <div class="bar"></div>
    </div>
</div>
"""


class AjaxUploadEditor(widgets.TextInput):

    class Media:
        js = (
            'ajaxupload/js/jquery.ui.widget.js',
            'ajaxupload/js/jquery.iframe-transport.js',
            'ajaxupload/js/jquery.fileupload.js',
            'ajaxupload/js/ajaxupload.js',
        )
        css = {
            'all': (
                'ajaxupload/css/bootstrap-progress.min.css',
                'ajaxupload/css/styles.css',
            )
        }

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        self.max_width = kwargs.pop('max_width', '')
        self.max_height = kwargs.pop('max_height', '')
        self.crop = kwargs.pop('crop', '')
        super(AjaxUploadEditor, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        
        kwargs = {'upload_to': self.upload_to,
                  'max_width': self.max_width,
                  'max_height': self.max_height,
                  'crop': self.crop}
        
        upload_url = reverse('ajaxupload', kwargs=kwargs)
        img_url = value if value else ''
        output = HTML % (upload_url, img_url, img_url, img_url, img_url, id_, name)
        return mark_safe(output)