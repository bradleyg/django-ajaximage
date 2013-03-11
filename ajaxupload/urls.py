from django.conf.urls.defaults import url, patterns

from ajaxupload.views import ajax_upload
from ajaxupload.forms import ImageForm


urlpatterns = patterns('',
    url('^upload/image/(?P<upload_to>.*)', ajax_upload, {
        'form_class': ImageForm,
        'response': lambda name, url: url,
    }, name='ajax_upload_image'),
)
