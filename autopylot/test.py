import autopylot
import unittest

class Testautopylot(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_enum(self):
        Wizard = autopylot.enum(MERLIN=1, GANDALF=2, SEVERUS_SNAPE=3, RINCEWIND=4, RAND_ALTHOR=5)
        self.assertIsInstance(Wizard, type)
        self.assertEqual(1, Wizard.MERLIN)
        self.assertEqual(2, Wizard.GANDALF)
        self.assertEqual(3, Wizard.SEVERUS_SNAPE)
        self.assertEqual(4, Wizard.RINCEWIND)
        self.assertEqual(5, Wizard.RAND_ALTHOR)

    def test_ignored_default(self):
        d = {}
        with autopylot.ignored():
            d[1]

    def test_ignored_keyerror(self):
        d = {}
        with autopylot.ignored(KeyError):
            d[1]

    def test_ignored_wrong_exception(self):
        def _raises_exc():
            d = {}
            with autopylot.ignored(IndexError):
                d[1]
        self.assertRaises(KeyError, _raises_exc)

if __name__ == '__main__':
    unittest.main(verbosity=2)
