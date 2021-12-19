import unittest

from morse import Morse 

class TestMorse(unittest.TestCase):
    def test_input(self):
        self.assertEqual(Morse('a'), "Wrong Character")
        self.assertEqual(Morse(6), "Wrong Character")
        self.assertEqual(Morse('.-'), "a")


if __name__ == "__main__":
    unittest.main()