from django.db import models
from ajaximage.fields import AjaxImageField


class Kitten(models.Model):
    thumbnail = AjaxImageField(upload_to='thumbnails',
                               max_height=200,
                               max_width=200,
                               crop=False)

    def __unicode__(self):
        # Cant return self.thumbnail - must first convert it to str
        # Either return url/path or str(self.thumbnail)
        return unicode(self.thumbnail)

    def __str__(self):
        return str(self.thumbnail)

    @property
    def url(self):
        return self.thumbnail.url

    @property
    def path(self):
        return self.thumbnail.path
