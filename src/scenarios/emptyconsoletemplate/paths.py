'''
This script fixes sys.path so tests can find shared libaries. It also configures logging.
It should not be changed
'''


import os
import sys

from os import environ

relativeshared = os.path.join('..', 'shared')
if(os.path.isdir(relativeshared)):
    sys.path.append(os.path.abspath(os.path.join('..', 'shared')))
    sys.path.append(os.path.abspath(os.path.join('..', '..', '..', 'scripts')))
    print(sys.path)
else:
    payload = environ.get('HELIX_CORRELATION_PAYLOAD')
    sys.path.append(os.path.join(payload, 'shared'))
    sys.path.append(os.path.join(payload, 'scripts'))

from performance.logger import setup_loggers
setup_loggers(True)
