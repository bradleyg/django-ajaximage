
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

try:
	from django.conf.urls import patterns, include, url
	urlpatterns = patterns('',
	    url(r'^admin/', include(admin.site.urls)),
	    url(r'^ajaximage/', include('ajaximage.urls')),
	    url(r'^form/', include('kitten.urls')),
	)
except ImportError:
	# django 1.10
	from django.conf.urls import include, url
	urlpatterns = [
	    url(r'^admin/', include(admin.site.urls)),
	    url(r'^ajaximage/', include('ajaximage.urls')),
	    url(r'^form/', include('kitten.urls')),
	]
	

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
