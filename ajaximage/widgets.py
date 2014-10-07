import os
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage


class AjaxImageWidget(widgets.TextInput):

    html = """
    <div class="ajaximage">
        <a class="file-link" target="_blank" href="{file_url}">
            <img class="file-img" src="{file_url}">
        </a>
        <a class="file-remove" href="#remove">Remove</a>
        <input class="file-path" type="hidden" value="{file_path}" id="{element_id}" name="{name}" />
        <input type="file" class="file-input" />
        <input class="file-dest" type="hidden" value="{upload_url}">
        <div class="progress progress-striped active">
            <div class="bar"></div>
        </div>
    </div>
    """

    class Media:
        js = (
            'ajaximage/js/ajaximage.js',
        )
        css = {
            'all': (
                'ajaximage/css/bootstrap-progress.min.css',
                'ajaximage/css/styles.css',
            )
        }

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        self.max_width = kwargs.pop('max_width', 0)
        self.max_height = kwargs.pop('max_height', 0)
        self.crop = kwargs.pop('crop', 0)
        super(AjaxImageWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        element_id = final_attrs.get('id')

        kwargs = {'upload_to': self.upload_to,
                  'max_width': self.max_width,
                  'max_height': self.max_height,
                  'crop': self.crop}

        upload_url = reverse('ajaximage', kwargs=kwargs)

        # NB convert to string and do not rely on value.url
        # value.url fails when rendering form with validation errors because
        # form value is not a FieldFile. Use storage.url and file_path - works
        # with FieldFile instances and string formdata
        file_path = str(value) if value else ''
        file_url = default_storage.url(file_path) if value else ''

        file_name = os.path.basename(file_url)

        output = self.html.format(upload_url=upload_url,
                             file_url=file_url,
                             file_name=file_name,
                             file_path=file_path,
                             element_id=element_id,
                             name=name)

        return mark_safe(output)
