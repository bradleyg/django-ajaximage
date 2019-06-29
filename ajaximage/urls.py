from django.urls import re_path
from ajaximage import views

urlpatterns = [
    re_path(r'^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
        views.ajaximage,
        name='ajaximage'),
]
