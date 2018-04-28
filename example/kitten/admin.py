from django.contrib import admin
from .models import Kitten
from django.utils.html import format_html

class KittenAdmin(admin.ModelAdmin):
    list_display = ['admin_thumb', '__str__', 'url', 'path']

    def admin_thumb(self, obj):
        return format_html('<img src="{0}" />'.format(obj.thumbnail.url))
    admin_thumb.allow_tags = True
    admin_thumb.short_description = 'Kitten Image'


admin.site.register(Kitten, KittenAdmin)
