from datetime import datetime

def unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    try:
        total_seconds = delta.total_seconds()
    except: # python < 2.7
        total_seconds = delta.days * 86400 + delta.seconds + delta.microseconds / 1e6
    return total_seconds

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0
