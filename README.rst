================
django-basicauth
================

Basic auth utilities for Django.

Requires
========

Tested under...

* Python

  * 3.4

* Django

  * 1.7
  * 1.8

Installation
============

::

    pip install django-basicauth


Usage
=====

.. code-block:: python

    from basicauth.decorators import basic_auth_required

    @basic_auth_required
    def myview(request):
        ...

Settings
========

* ``BASICAUTH_USE_DICT``: Use BASICAUTH_USERS for authentication.
* ``BASICAUTH_USERS``: Dictionary including keys as username and values as passwords.
* ``BASICAUTH_USE_DJANGO_AUTH``: Use django's builtin authentication.
* ``BASICAUTH_REALM``: realm string, default is "Secure resource".
