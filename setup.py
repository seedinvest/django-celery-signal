from setuptools import setup, find_packages
setup(
    name='django-celery-signal',
    version=__import__('django_celery_signal').get_version(limit=3),
    description='Async signal for celery',
    author='Eamonn Faherty',
    author_email='github@designandsolve.co.uk',
    url='https://github.com/eamonnfaherty/django-celery-signal',
    license='MIT',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Utilities',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False
)
