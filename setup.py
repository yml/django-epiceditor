from setuptools import setup


setup(
  name = "django-epiceditor",
  version = "0.2.1.2",
  author = "Remi Barraquand",
  author_email = "dev@remibarraquand.com",
  url = "https://github.com/barraq/django-epiceditor",
  description = ("A django app that allows the easy addition of EpicEditor markdown editor to a django form field, whether in a custom app or the Django Admin."),
  long_description = open('README.rst').read(),
  packages = ['epiceditor'],
  include_package_data = True,
  install_requires = [
    "Django >= 1.3",
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    ],
  license='LICENSE',
)
