from .views import MyView

try:
	from django.conf.urls import patterns, url
	urlpatterns = patterns('',
	    url('', MyView.as_view(), name='form'),
	)
except ImportError:
  	# django 1.10
	from django.conf.urls import url
	urlpatterns = [
	    url('', MyView.as_view(), name='form'),
	]
