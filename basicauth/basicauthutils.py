from __future__ import absolute_import
import base64
import binascii
from urllib import unquote_plus
from itertools import imap


def extract_basicauth(authorization_header, encoding=u'utf-8'):
    splitted = authorization_header.split(u' ')
    if len(splitted) != 2:
        return None

    auth_type, auth_string = splitted

    if u'basic' != auth_type.lower():
        return None

    try:
        b64_decoded = base64.b64decode(auth_string)
    except (TypeError, binascii.Error):
        return None
    try:
        auth_string_decoded = b64_decoded.decode(encoding)
    except UnicodeDecodeError:
        return None

    splitted = auth_string_decoded.split(u':')

    if len(splitted) != 2:
        return None

    username, password = imap(unquote_plus, splitted)
    return username, password
