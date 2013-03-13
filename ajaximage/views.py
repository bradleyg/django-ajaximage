import os, json

from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ajaximage.image import resize
from ajaximage.forms import FileForm


UPLOAD_PATH = getattr(settings, 'AJAXIMAGE_DIR', 'ajaximage/')


@csrf_exempt
@require_POST
@user_passes_test(lambda u: u.is_staff)
def ajaximage(request, upload_to=None, max_width=None, max_height=None, crop=None, form_class=FileForm, response=lambda name, url: url):
    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        file_ = form.cleaned_data['file']
        
        image_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/pjpeg', 'image/gif']
        if file_.content_type not in image_types:
            return HttpResponse(status=403, content='Bad image format')

        file_ = resize(file_, max_width, max_height, crop)
        file_name, extension = os.path.splitext(file_.name)
        file_name = "".join([c for c in file_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        safe_name = '{0}{1}'.format(file_name, extension)
        
        file_path = default_storage.save(os.path.join(upload_to or UPLOAD_PATH, safe_name), file_)
        url = os.path.join(settings.MEDIA_URL, file_path)
        
        return HttpResponse(json.dumps({'url': url}))
    return HttpResponse(status=403)
