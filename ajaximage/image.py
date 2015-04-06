import os
from PIL import Image, ImageOps
try:
    from StringIO import StringIO as IO
except ImportError:
    from io import BytesIO as IO

from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile


def resize(file_, max_width=0, max_height=0, crop=0):
    max_width = int(max_width)
    max_height = int(max_height)
    crop = int(crop)

    if(max_width is 0 and max_height is 0):
        return file_

    max_width = 9999 if max_width is 0 else max_width
    max_height = 9999 if max_height is 0 else max_height

    size = (max_width, max_height)
    image = Image.open(file_)

    if(image.mode == 'RGBA'):
        image.load()
        background = Image.new('RGB', image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])
        image = background

    temp = IO()

    if(crop is 1):
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
    else:
        image.thumbnail(size, Image.ANTIALIAS)

    image.save(temp, 'jpeg')
    temp.seek(0)

    return SimpleUploadedFile(file_.name,
                              temp.read(),
                              content_type='image/jpeg')