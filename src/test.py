import unittest
import sample

class TestCaculatorMethods(unittest.TestCase):
    def test_add(self):
        ca = sample.Caculator(2,3)
        self.assertEqual(5,ca.add())
    def test_add(self):
        ca = sample.Caculator(5,3)
        self.assertEqual(8,ca.add())

if __name__ == '__main__':
    unittest.main()
