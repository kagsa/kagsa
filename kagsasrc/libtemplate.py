# import some modules for "exec_data"
import re,os,sys,traceback,zipfile

# add "kagsasrc" path to "sys.path"
class Paths:
    def __path__ ():
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        # or a script file (e.g. `.py` / `.pyw`)
        elif __file__:
            return os.path.dirname(__file__)

    def init () :
        sys.path.insert(1, os.getcwd() )
        sys.path.insert(1, Paths.__path__() )

    def getFile (filen,mode):
        '''if Paths.AsPackage:
            pkg_path = os.path.dirname( pkg_resources.resource_stream(__name__,'errors.py').name ) + os.sep
            return open(pkg_path + filen,mode,encoding='utf-8')
        else:
            return open( Paths.__path__() + os.sep + filen, mode , encoding='utf-8')'''
        return open( Paths.__path__() + os.sep + filen, mode , encoding='utf-8')


#os.path.append(os.path.dirname( Paths.__path__() ))

from errors import __init__ as errors
from parse_id import __init__ as parse_id
from built_modules import *
from methods import *


