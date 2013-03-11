import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-ajaxupload',
    version='0.0.2',
    description='Ajax upload for images',
    long_description=readme,
    author="Bradley Griffiths",
    author_email='bradley.griffiths@gmail.com',
    url='https://github.com/bradleyg/django-ajaxupload',
    packages=['ajaxupload'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)