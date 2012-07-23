Django Boilerplate (Updated for Django 1.4)
===========================================

A barebones default layout for organised Django development. Inspired a little by Ruby on Rails and 'Django Project Conventions by Zachary Voase (link below).


### Usage

This assumes you have pip and django installed (if not, try `$ sudo easy_install pip`)

    $ django-admin.py startproject --template http://github.com/martinogden/django-boilerplate/zipball/master project_name
    $ cd project_name
    $ pip install -r REQUIREMENTS
    $ python manage.py syncdb --migrate


### Settings

There is a separate file for each environment inside `config/environments` (development, staging, production). These import the django default settings from config.settings and are intended to be used directly, e.g. `python manage.py validate --settings=config.environments.production` or `export PYTHONPATH=config.environments.development`.

Any settings added in `environments/local.py` will be picked up and override any previously defined settings. This is useful for sensitive information such as database credentials or the `SECRET_KEY` etc. By default this file will *NOT* be checked into git.


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

