from contextdecorator import ContextDecorator
from django.core.cache import cache
from requests.exceptions import Timeout
import json
import logging
import requests

logger = logging.getLogger('caldwellpy')

class prime_cache(ContextDecorator):

    def __init__(self, cache_key, data_source, expire=60*60*24, timeout=10.0):
        self.cache_key = cache_key
        self.data_source = data_source
        self.expire = expire
        self.timeout = timeout

    def __enter__(self):
        data = cache.get(self.cache_key)

        if not data:
            try:
                resp = requests.get(self.data_source, timeout=self.timeout)

                if resp.status_code == requests.codes.ok:
                    try:
                        data = json.loads(resp.text)
                        cache.set(self.cache_key, data, self.expire)
                    except Exception, e:
                        logger.error('Error initializing cache: %s' % e)
                else:
                    logger.error('connection failed for url[%s] code[%s] msg[%s]' % (
                        self.data_source, resp.status_code, resp.text))

            except Timeout:
                logger.error('connection timeout for url[%s]' % self.data_source)

        return self

    def __exit__(self, type, value, traceback):
        return False
