from __future__ import absolute_import
from django.conf import settings
from django.http import HttpResponse


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

    def __init__(self):
        super(HttpResponseUnauthorized, self).__init__(
            u"""<html><head><title>Basic auth required</title></head>
               <body><h1>Authorization Required</h1></body></html>""",
        )
        realm = getattr(settings, u'BASICAUTH_REALM', u'Secure resource')
        self[u'WWW-Authenticate'] = u'Basic realm="{}"'.format(realm)
