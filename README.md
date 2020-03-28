django-ajaximage
===============

Ajax image uploads.
-------------------------------------

Upload images via ajax. Images are optionally resized.

Optimized on https://github.com/bradleyg/django-ajaximage.

Features Appended:

* Correctly display the readonly field
* Support django2 and above
* `upload_to` support datetime string format
* Change FileField to ImageFileField to compatible with ImageField
* Add format_image method to display custom image field using the same format
    ```
    from ajaximage.utils import format_image
    class xxxAdmin(ModelAdmin):
        ...
        def some_field(obj):
            return format_image(obj.some_field.ajaximagefield)      
    ```

![screenshot](/screenshot.png?raw=true)

## Support
Python 3
Django > 2.0
Chrome / Safari / Firefox / IE10+


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
urlpatterns += [
    path('ajaximage/', include('ajaximage.urls')),
]
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

$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Visit ```http://localhost:8000/admin``` to view the admin widget and ```http://localhost:8000/form``` to view the custom form widget.
