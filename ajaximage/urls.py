try:  # pre 1.10
    from django.conf.urls import url, patterns
    urlpatterns = patterns(
        '',
        url(
            '^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
            'ajaximage.views.ajaximage', name='ajaximage'
        ),
    )

except ImportError:
    from django.conf.urls import url
    from ajaximage.views import ajaximage

    urlpatterns = (
        url(
            '^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
            ajaximage, name='ajaximage'
        ),
    )
