Django Boilerplate
==================

A barebones default layout for organised Django development.


### Quick install

This assumes you have pip installed (if not, try `$ sudo easy_install pip`)

    $ git clone git://github.com/martinogden/django-boilerplate.git
    $ pip install -r REQUIREMENTS
    $ python manage.py syncdb --settings=settings.development


### Settings

There is a separate file for each environment `settings` (development, staging, production). These import the django default settings from settings.common and are intended to be used directly, e.g. `python manage.py validate --settings=settings.production` or `export PYTHONPATH=settings.development`.


### Preinstalled Apps

 * [path.py](https://github.com/dottedmag/path.py): A module wrapper for os.path
 * [South](http://south.aeracode.org/): Intelligent database migrations
 * [django-grappelli](https://github.com/sehmaschine/django-grappelli): A jazzy skin for the Django admin interface.
 * [django-command-extensions](https://github.com/django-extensions): A a collection of custom extensions 
 * [fabric](http://docs.fabfile.org/en/1.3.1/index.html): Application deployment and systems administration tasks.
 * [django-compressor](https://github.com/jezdez/django_compressor): Compresses linked and inline javascript or CSS into a single cached file.


### Credits

Much of the layout is taken from a great [post](http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/) by Zachary Voase.


### Contributors

 * [Scotty Vernon](http://twitter.com/KingScooty): django-compressor integration, included modernizr, boilerplate markup in base.html, and organised javascripts folder.


### Licence

Licensed for use under BSD (same as [Django](https://code.djangoproject.com/browser/django/trunk/LICENSE)).
