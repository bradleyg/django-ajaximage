from django.conf.urls.defaults import url, patterns

from ajaxupload.views import ajax_upload
from ajaxupload.forms import ImageForm


urlpatterns = patterns('',
    url('^upload/(?P<upload_to>.*)', ajaxupload, {
        'form_class': ImageForm,
        'response': lambda name, url: url,
    }, name='ajaxupload'),
)
