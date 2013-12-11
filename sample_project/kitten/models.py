from django.db import models
from ajaximage.fields import AjaxImageField


class Kitten(models.Model):
    thumbnail = AjaxImageField(upload_to='thumbnails',
                               max_height=200,
                               max_width=200,
                               crop=False)

    def __unicode__(self):
        return self.thumbnail
