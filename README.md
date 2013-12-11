##Ajax file uploads
  
[https://github.com/bradleyg/django-ajaximage](https://github.com/bradleyg/django-ajaximage)
  
Add ajax image upload functionality with a progress bar to file input fields within Django admin. Images are optionally resized.

![screenshot](https://raw.github.com/bradleyg/django-ajaximage/master/screenshot.png)

```pip install django-ajaximage```

```python
# settings.py
AJAXIMAGE_DIR = 'ajaximage/' # (optional, default is 'ajaximage/')
AJAXIMAGE_PREPEND_MEDIA_URL = True # (optional, default is 'True')

INSTALLED_APPS = [
    # 
    'ajaximage',
]
```
  
```python
# urls.py
urlpatterns = patterns('',
    url(r'^ajaximage/', include('ajaximage.urls')),
)
```
  
```python
# models.py
from django.db import models
from ajaximage.fields import AjaxImageField

class Example(models.Model):
    thumbnail = AjaxImageField(upload_to='thumbnails'
                               max_height=200, #optional
                               max_width=200, # optional
                               crop=True) # optional
                               
# if crop is provided both max_height and max_width are required
```

Rememeber to call ``collectstatic`` in order to made available the javascript
files necessary to the admin field.
