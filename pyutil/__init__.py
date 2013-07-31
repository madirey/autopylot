from contextlib import contextmanager
from .enum import *

@contextmanager
def ignored(*exceptions):
    ''' inspired by http://hg.python.org/cpython/rev/406b47c64480'''
    exceptions = exceptions or Exception
    try:
        yield
    except exceptions:
        pass
