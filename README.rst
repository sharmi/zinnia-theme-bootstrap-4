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


.. _`Bootstrap 3`: http://getbootstrap.com/
.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`django-app-namespace-template-loader`: https://github.com/Fantomas42/django-app-namespace-template-loader
.. _`Zinnia is installed`: http://docs.django-blog-zinnia.com/en/latest/getting-started/install.html
.. _`Zinnia Theme Bootstrap`: https://github.com/django-blog-zinnia/zinnia-theme-bootstrap

