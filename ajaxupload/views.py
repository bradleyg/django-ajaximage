import os, hashlib, json

from django.conf import settings
from django.utils.encoding import smart_str
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ajaxupload.forms import FileForm


UPLOAD_PATH = getattr(settings, 'AJAXUPLOAD', 'ajaxupload/')


@csrf_exempt
@require_POST
@user_passes_test(lambda u: u.is_staff)
def ajaxupload(request, upload_to=None, form_class=FileForm, response=lambda name, url: url):
    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        file_ = form.cleaned_data['file']
        
        image_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/pjpeg', 'image/gif']
        file_type = 'image' if file_.content_type in image_types else 'file'
            
        file_name, extension = os.path.splitext(file_.name)
        m = hashlib.md5(smart_str(file_name))
        hashed_name = '{0}{1}'.format(m.hexdigest(), extension)
        file_path = default_storage.save(os.path.join(upload_to or UPLOAD_PATH, hashed_name), file_)
        url = os.path.join(settings.MEDIA_URL, file_path)
        
        return HttpResponse(json.dumps({'url': url, 'file_type': file_type}))
    return HttpResponse(status=403)
