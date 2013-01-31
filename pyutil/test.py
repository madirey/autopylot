import pyutil
import unittest

class TestPyUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_enum(self):
        Wizard = pyutil.enum(MERLIN=1, GANDALF=2, SEVERUS_SNAPE=3, RINCEWIND=4, RAND_ALTHOR=5)
        self.assertIsInstance(Wizard, type)
        self.assertEqual(1, Wizard.MERLIN)
        self.assertEqual(2, Wizard.GANDALF)
        self.assertEqual(3, Wizard.SEVERUS_SNAPE)
        self.assertEqual(4, Wizard.RINCEWIND)
        self.assertEqual(5, Wizard.RAND_ALTHOR)


if __name__ == '__main__':
    unittest.main(verbosity=2)
