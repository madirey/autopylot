from contextlib import contextmanager
from .enum import *
import urlparse

@contextmanager
def ignored(*exceptions):
    ''' inspired by http://hg.python.org/cpython/rev/406b47c64480'''
    exceptions = exceptions or Exception
    try:
        yield
    except exceptions:
        pass

def formaturl(url):
    parsed = list(urlparse.urlparse(url))
    parsed[2] = parsed[2].replace('//', '/')
    return urlparse.urlunparse(parsed)
