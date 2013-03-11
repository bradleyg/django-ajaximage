```python
from django.db import models
from ajaxupload.fields import AjaxUploadField

class Example(models.Model):
    thumbnail = AjaxUploadField(upload_to='thumbnails')
```