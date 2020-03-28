import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django2-ajaximage',
    version='0.7.0',
    description='Upload images via ajax. Images are optionally resized.',    
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Bradley Griffiths(Modified by Daimon)",
    author_email='bradley.griffiths@gmail.com',
    url='https://github.com/bradleyg/django2-ajaximage',
    packages=['ajaximage'],
    include_package_data=True,
    install_requires=['Django', 'Pillow',],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
    ],
)
