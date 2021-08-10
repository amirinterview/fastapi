import unittest
from main import addition


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(addition(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
