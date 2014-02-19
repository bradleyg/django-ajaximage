try:  # pre 1.6
    from django.conf.urls.defaults import url, patterns
except ImportError:
    from django.conf.urls import url, patterns

from .forms import FileForm

urlpatterns = patterns(
    '',
    url(
        '^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
        'ajaximage.views.ajaximage',
        {'form_class': FileForm},
        name='ajaximage'
    ),
)
