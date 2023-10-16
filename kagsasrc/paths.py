import sys
import os

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
            return open(os.path.join(Paths.__path__(), filen), mode, encoding='utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filen}' not found.")
