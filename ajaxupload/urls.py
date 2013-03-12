from django.conf.urls.defaults import url, patterns

from ajaxupload.views import ajaxupload
from ajaxupload.forms import FileForm


urlpatterns = patterns('',
    url('^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)', ajaxupload, {
        'form_class': FileForm,
        'response': lambda name, url: url,
    }, name='ajaxupload'),
)
