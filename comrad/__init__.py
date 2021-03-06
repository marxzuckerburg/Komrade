# basic config
from .constants import *
from .utils import *
from .cli.artcode import *

# common python imports
import os,sys
from collections import defaultdict
from base64 import b64encode,b64decode
import json
import binascii,asyncio
from pprint import pprint


# common external imports
from pythemis.skeygen import KEY_PAIR_TYPE, GenerateKeyPair
from pythemis.smessage import SMessage, ssign, sverify
from pythemis.skeygen import GenerateSymmetricKey
from pythemis.scell import SCellSeal
from pythemis.exception import ThemisError


try:
    import getch
    def getpass(prompt):
        """Replacement for getpass.getpass() which prints asterisks for each character typed"""
        print(prompt, end='', flush=True)
        buf = ''
        while True:
            ch = getch.getch()
            if ch == '\n':
                print('')
                break
            else:
                buf += ch
                print('*', end='', flush=True)
        return buf
except ImportError:
    from getpass import getpass

from backend import *