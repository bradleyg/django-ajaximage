from django.conf.urls.defaults import url, patterns

from ajaximage.views import ajaximage
from ajaximage.forms import FileForm


urlpatterns = patterns('',
    url('^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)', ajaximage, {
        'form_class': FileForm,
        'response': lambda name, url: url,
    }, name='ajaximage'),
)
