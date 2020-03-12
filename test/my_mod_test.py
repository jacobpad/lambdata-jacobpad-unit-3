import unittest
from my_lambdata.my_mod import ten_x

class TestMyMod(unittest.TestCase):

    def test_ten_x(self):
        self.assertEqual(ten_x(10), 100)

if __name__ == '__main__':
    unittest.main()