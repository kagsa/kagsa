import pkg_resources,os,sys

# from .paths import Paths as Paths
# Paths.init()
# Paths.getFile(  )

class Paths:
    AsPackage = True
    if getattr(sys, 'frozen', False):
        __path__ = os.path.dirname(sys.executable)
    # or a script file (e.g. `.py` / `.pyw`)
    elif __file__:
        __path__ = os.path.dirname(__file__)

    def init () :
        if not(Paths.AsPackage):
            sys.path.append( os.getcwd() )
            sys.path.append( __path__ )

    def getFile (filen,mode):
        if Paths.AsPackage:
            pkg_path = os.path.dirname( pkg_resources.resource_stream(__name__,'errors.py').name ) + os.sep
            return open(pkg_path + filen,mode,encoding='utf-8')
        else:
            return open( __path__ + os.sep + filen, mode , encoding='utf-8')


#pkg_resources.resource_stream(__name__,'built_modules.py').read().decode('utf-8')