# from http://stackoverflow.com/users/22364/markus-jarderot
def first(iterable, default=None):
    for item in iterable:
        return item
    return default
