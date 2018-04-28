from django.urls import path

from .views import MyView


urlpatterns = [
    path('', MyView.as_view(), name='form'),
]
