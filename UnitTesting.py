import unittest
import PROJCODE

class TestMorseTranslation(unittest.TestCase):

#ENCRYPTION CASES 

    def test_encryption(characters):
        characters.assertEqual(PROJCODE.encryption("AHMED"), ".- .... -- . -.. ")
        characters.assertEqual(PROJCODE.encryption("FAHMI 2005"), "..-. .- .... -- .. | ..--- ----- ----- ..... ")

    def test_incorrect_user_input_e(characters):
        characters.assertEqual(PROJCODE.encryption("$%^&*@"), "######")

    def test_unidentifiable_characters_e(characters):
        characters.assertEqual(PROJCODE.encryption("7 PERCENT %"), "--... | .--. . .-. -.-. . -. - | #")
        characters.assertEqual(PROJCODE.encryption("1 dollar $"), ".---- | -.. --- .-.. .-.. .- .-. | #")

    def test_case_sensitivity(characters):
        characters.assertEqual(PROJCODE.encryption("uppercase"), "..- .--. .--. . .-. -.-. .- ... . ")
        characters.assertEqual(PROJCODE.encryption("UppErCaSe"), "..- .--. .--. . .-. -.-. .- ... . ")
        
    def test_empty_string_e(characters):
        characters.assertEqual(PROJCODE.encryption(""), "")

    def test_phrase_incl_punctuation_e(characters):
        characters.assertEqual(PROJCODE.encryption("WHO, IS. THIS! MAN?"), ".-- .... --- --..-- | .. ... .-.-.- | - .... .. ... -.-.-- | -- .- -. ..--.. ")


#DECRYPTION CASES
     
    def test_decryption(characters):
        characters.assertEqual(PROJCODE.decryption(".- -... -.-."), "ABC")
        characters.assertEqual(PROJCODE.decryption(".- -... -.-. | ..--- ----- ----- ....."), "ABC 2005")

    def test_phrase_incl_punctuation_d(characters):
        characters.assertEqual(PROJCODE.decryption(".-- .... --- --..-- | .. ... .-.-.- | - .... .. ... -.-.-- | -- .- -. ..--.."), "WHO, IS. THIS! MAN?")

    def test_incorrect_user_input_d(characters):
        characters.assertEqual(PROJCODE.decryption("--.-- .---.-.- .--.-"), "###")

    def test_unidentifiable_characters_d(characters):
        characters.assertEqual(PROJCODE.decryption(".- -... -.-. ---.-"), "ABC#")

if __name__ == '__main__':
    unittest.main()
