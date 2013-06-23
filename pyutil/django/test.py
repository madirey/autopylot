from django.conf import settings

settings.configure(
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }, DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_pyutil',
        }
    }
)

from contextlib import contextmanager
from django.core.cache import cache
from django.test import TestCase
from mock import patch
from templatetags import pyutil
import contextmanagers

@contextmanager
def mock_request(status_code=200, text=''):
    patch_requests = patch.object(contextmanagers, 'requests',
                                  _MockRequests(status_code, text))
    patch_requests.start()
    yield
    patch_requests.stop()


class _MockRequests(object):
    class _MockResponseCodes(object):
        ok = 200
        not_ok = 400

    class _MockResponse(object):

        def __init__(self, status_code, text):
            self.status_code = status_code
            self.text = text

    def __init__(self, status_code=200, text='{}'):
        self.codes = self._MockResponseCodes()
        self.text = text
        self.status_code = status_code

    def get(self, url, timeout):
        resp = self._MockResponse(self.status_code, self.text)
        return resp

class TestDjango(TestCase):
    def setUp(self):
        cache.clear()

    def tearDown(self):
        cache.clear()

    def test_get_cached_not_cached(self):
        with mock_request(200, '[{"answer": 42}]'):
            with contextmanagers.get_cached('test_pyutil',
                                            'http://notreal.com/fake')\
                                            as parsed_json:
                expected = [{'answer': 42}]
                self.assertEqual(expected, parsed_json)
                self.assertEqual(expected, cache.get('test_pyutil'))

    def test_get_cached_cached(self):
        with mock_request(200, 'not-valid-json'):
            expected = [{'answer': 42}]
            cache.set('test_pyutil', expected)
            self.assertEqual(expected, cache.get('test_pyutil'))
            with contextmanagers.get_cached('test_pyutil',
                                            'http://notreal.com/fake')\
                                            as parsed_json:
                self.assertEqual(expected, parsed_json)

    def test_get_cached_bad_response(self):
        with mock_request(400, '{"valid": "json"}'):
            with contextmanagers.get_cached('test_pyutil',
                                            'http://notreal.com/fake')\
                                            as parsed_json:
                self.assertEqual(None, parsed_json)

    def test_get_cached_invalid_json_response(self):
        with mock_request(200, 'invalid-json'):
            with contextmanagers.get_cached('test_pyutil',
                                            'http://notreal.com/fake',
                                            default=[])\
                                            as parsed_json:
                self.assertEqual([], parsed_json)

    def test_get_cached_timeout(self):
        with contextmanagers.get_cached('test_pyutil',
                                        'http://localhost/notreal/fake',
                                        timeout=0.00001)\
                                        as parsed_json:
            self.assertEqual(None, parsed_json)

    def test_get_key_found(self):
        self.assertEqual(2, pyutil.getkey({1:2}, 1))

    def test_get_key_notfound(self):
        self.assertEqual('', pyutil.getkey({1:2}, 2))

    def test_split(self):
        self.assertEqual(['1','2','3'], pyutil.split('1,2,3', ','))
