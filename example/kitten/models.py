from django.db import models
from ajaximage.fields import AjaxImageField


class Kitten(models.Model):
    image = AjaxImageField()
    thumbnail = AjaxImageField(upload_to='thumbnails', max_height=200,
                               max_width=200, crop=False)

    def __str__(self):
        return str(self.thumbnail)

    @property
    def url(self):
        return self.thumbnail.url

    @property
    def path(self):
        return self.thumbnail.path
