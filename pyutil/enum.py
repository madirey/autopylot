# from http://stackoverflow.com/a/1695250/163789 (thanks!)

def enum(**mappings):
    return type('Enum', (), mappings)
