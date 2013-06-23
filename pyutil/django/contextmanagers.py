from contextlib import contextmanager
from django.core.cache import cache
from requests.exceptions import Timeout
import json
import logging
import requests

logger = logging.getLogger('caldwellpy')

@contextmanager
def get_cached(cache_key, data_source, default=None, expire=60*60*24, timeout=10.0):
    data = cache.get(cache_key)
    if not data:
        try:
            resp = requests.get(data_source, timeout=timeout)

            if resp.status_code == requests.codes.ok:
                try:
                    data = json.loads(resp.text)
                    cache.set(cache_key, data, expire)
                except Exception, e:
                    logger.error('Error initializing cache: %s' % e)
            else:
                logger.error('connection failed for url[%s] code[%s] msg[%s]' % (
                    data_source, resp.status_code, resp.text))

        except Timeout:
            logger.error('connection timeout for url[%s]' % data_source)

        except Exception, e:
            logger.error('connection error[%s]' % e)

    yield data or default
