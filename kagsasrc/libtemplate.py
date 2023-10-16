import os
import sys

class Paths:
    @staticmethod
    def __path__():
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        elif __file__:
            return os.path.dirname(__file__)

    @staticmethod
    def init():
        sys.path.insert(1, os.getcwd())
        sys.path.insert(1, Paths.__path__())

    @staticmethod
    def getFile(filen, mode):
        try:
            file_path = os.path.join(Paths.__path__(), filen)
            return open(file_path, mode, encoding='utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f'File "{filen}" not found.')

Paths.init()

from errors import __init__ as errors
from parse_id import __init__ as parse_id
from built_modules import *
from methods import *
