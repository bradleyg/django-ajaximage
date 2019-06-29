from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajaximage/', include('ajaximage.urls')),
    path('form/', include('kitten.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
