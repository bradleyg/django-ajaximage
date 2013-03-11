from django.conf.urls.defaults import url, patterns

from ajaxupload.views import ajaxupload
from ajaxupload.forms import FileForm


urlpatterns = patterns('',
    url('^upload/(?P<upload_to>.*)', ajaxupload, {
        'form_class': FileForm,
        'response': lambda name, url: url,
    }, name='ajaxupload'),
)
