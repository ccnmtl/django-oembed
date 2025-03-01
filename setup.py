from __future__ import unicode_literals

from setuptools import setup, find_packages
 
setup(
    name='django-oembed',
    version='0.1.5',
    description='A collection of Django tools which make it easy to change text filled with oembed links into the embedded objects themselves.',
    author='Eric Florenzano',
    author_email='floguy@gmail.com',
    url='https://github.com/ccnmtl/django-oembed',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests.runtests',
)
