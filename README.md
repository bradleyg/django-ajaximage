##Ajax file uploads

Add ajax upload functionality with a progress bar to file input fields within Django admin.

![screenshot](https://raw.github.com/bradleyg/django-ajaxupload/master/screenshot.png)

```pip install django-ajaxupload```

```python
# settings.py
AJAXUPLOAD = 'uploads/' # (optional, default is 'ajaxupload/')
```

```python
# models.py
from django.db import models
from ajaxupload.fields import AjaxUploadField

class Example(models.Model):
    thumbnail = AjaxUploadField(upload_to='thumbnails')
```
