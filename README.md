django-ajaximage
===============

Ajax image uploads.
-------------------------------------

[![PyPi Version](https://pypip.in/v/django-ajaximage/badge.png)](https://crate.io/packages/django-ajaximage)
[![PyPi Downloads](https://pypip.in/d/django-ajaximage/badge.png)](https://crate.io/packages/django-ajaximage)

Upload images via ajax. Images are optionally resized.

![screenshot](https://raw.githubusercontent.com/bradleyg/django-ajaximage/master/screenshot.png)

## Support
Python 2/3
Chrome / Safari / Firefox / IE10+

For older browser support use version 0.1.18.

## Installation

Install with Pip:

```pip install django-ajaximage```

## Django Setup

### settings.py

```python
INSTALLED_APPS = [
    ...
    'ajaximage',
    ...
]

# Settings
AJAXIMAGE_AUTH_TEST = lambda u: True
```

### urls.py

```python
urlpatterns = patterns('',
    url(r'^ajaximage/', include('ajaximage.urls')),
)
```

Run ```python manage.py collectstatic``` if required.

## Use in Django admin only

### models.py

```python
from django.db import models
from ajaximage.fields import AjaxImageField

class Example(models.Model):
    thumbnail = AjaxImageField(upload_to='thumbnails',
                               max_height=200, #optional
                               max_width=200, # optional
                               crop=True) # optional

# if crop is provided both max_height and max_width are required
```

## Use the widget in a custom form

### forms.py

```python
from django import forms
from ajaximage.widgets import AjaxImageWidget

class AjaxImageUploadForm(forms.Form):
    images = forms.URLField(widget=AjaxImageWidget(upload_to='form-uploads'))
```

### views.py

```python
from django.views.generic import FormView
from .forms import AjaxImageUploadForm

class MyView(FormView):
    template_name = 'form.html'
    form_class = AjaxImageUploadForm
```

### templates/form.html

```html
<html>
<head>
    <meta charset="utf-8">
    <title>ajaximage</title>
    {{ form.media }}
</head>
<body>
    {{ form.as_p }}
</body>
</html>
```

## Examples
Examples of both approaches can be found in the examples folder. To run them:
```shell
$ git clone git@github.com:bradleyg/django-ajaximage.git
$ cd django-ajaximage
$ python setup.py install
$ cd example

$ python manage.py syncdb
$ python manage.py runserver 0.0.0.0:5000
```

Visit ```http://localhost:5000/admin``` to view the admin widget and ```http://localhost:5000/form``` to view the custom form widget.