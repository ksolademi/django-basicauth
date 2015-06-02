from __future__ import absolute_import
from functools import wraps

from django.conf import settings
from django.contrib.auth import authenticate, login

from basicauth.basicauthutils import extract_basicauth
from basicauth.response import HttpResponseUnauthorized


def basic_auth_required(func):
    @wraps(func)
    def _wrapped(request, *args, **kwargs):
        if u'HTTP_AUTHORIZATION' not in request.META:
            return HttpResponseUnauthorized()

        authorization_header = request.META[u'HTTP_AUTHORIZATION']
        ret = extract_basicauth(authorization_header)
        if not ret:
            return HttpResponseUnauthorized()

        username, password = ret

        if settings.BASICAUTH_USE_DJANGO_AUTH:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.user = user
                    return func(request, *args, **kwargs)

            return HttpResponseUnauthorized()

        if (settings.BASICAUTH_USE_DICT and
                settings.BASICAUTH_USERS.get(username) != password):
            return HttpResponseUnauthorized()

        return func(request, *args, **kwargs)
    return _wrapped
