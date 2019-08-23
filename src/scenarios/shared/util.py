'''
Utility routines
'''
import sys
import os
from os import environ
from shared import const

def helixpayload():
    '''
    Returns the helix payload. Will be None outside of helix.
    '''
    return environ.get('HELIX_CORRELATION_PAYLOAD')

def extension():
    return '.exe' if sys.platform == 'win32' else ''

def appbin():
    return os.path.join(const.BINDIR, '%s%s' % (const.BINDIR, extension()))

def pubbin():
    return os.path.join(const.PUBDIR, '%s%s' % (const.BINDIR, extension()))