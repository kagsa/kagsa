import sys,os

# from .paths import Paths as Paths
# Paths.init()
# Paths.getFile(  )

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


#pkg_resources.resource_stream(__name__,'built_modules.py').read().decode('utf-8')