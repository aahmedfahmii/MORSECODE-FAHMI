import unittest
import PROJCODE

class TestMorseCodeConversion(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(PROJCODE.encryption("AHMED"), ".-....--.-..")
        self.assertEqual(PROJCODE.encryption("FAHMI 2005"), "..-..-....--..|..-------------.....")

    def test_decryption(self):
        self.assertEqual(PROJCODE.decryption(".- -... -.-."), "ABC")
        self.assertEqual(PROJCODE.decryption(".- -... -.-. | ..--- ----- ----- ....."), "ABC 2005")


if __name__ == '__main__':
    unittest.main()
