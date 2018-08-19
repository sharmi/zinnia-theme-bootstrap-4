======================
Zinnia-theme-bootstrap
======================

Zinnia-theme-bootstrap-4 is a python package providing a theme built on
`Bootstrap 4` for `django-blog-zinnia`_.
This is forked and adapted from `Zinnia Theme Bootstrap` 

Installation
============

First of all you need to install and configure
`django-app-namespace-template-loader`_ into your project.

The once `Zinnia is installed`_ on your Django project and this package
installed on your `PYTHON_PATH`, simply register the `zinnia_bootstrap4`
application in the `INSTALLED_APP` section of your project's settings.

Now Zinnia is Bootstrap ready.

.. warning::
   * `zinnia_bootstrap4` must be registered before the `zinnia` app to bypass
     the loading of the Zinnia's templates.
   * You need to use the ``django.template.loaders.eggs.Loader`` template
     loader if you have installed the package as an egg.

Setting up Demo
===============

To try out the demo, create a virtual environment. This is recommended but not necessary. The recommended python version is 3.

Either clone or download this repository
   
   `git clone https://github.com/sharmi/zinnia-theme-bootstrap-4.git`

   `export PYTHONPATH=/path/to/clone/location/zinnia-theme-bootstrap-4`

Next, install the following libraries

    `pip install django django-blog-zinnia django-app-namespace-template-loader zinnia-theme-bootstrap-4`

now run the following command to create the required tables.
 
    `django-admin migrate --settings "demo_zinnia_bootstrap.settings"`

Run the following command if you want an user id and password to login to the admin section. 

   `django-admin createsuperuser --settings "demo_zinnia_bootstrap.settings"`

Run the following command to start the server

   `django-admin runserver --settings "demo_zinnia_bootstrap.settings"`


.. _`Bootstrap 3`: http://getbootstrap.com/
.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`django-app-namespace-template-loader`: https://github.com/Fantomas42/django-app-namespace-template-loader
.. _`Zinnia is installed`: http://docs.django-blog-zinnia.com/en/latest/getting-started/install.html
.. _`Zinnia Theme Bootstrap`: https://github.com/django-blog-zinnia/zinnia-theme-bootstrap

