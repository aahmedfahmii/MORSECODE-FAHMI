import unittest
import PROJCODE

class TestMorseTranslation(unittest.TestCase):

#ENCRYPTION CASES 

    def test_encryption(characters):
        characters.assertEqual(PROJCODE.encryption("AHMED"), ".- .... -- . -.. ")
        characters.assertEqual(PROJCODE.encryption("FAHMI 2005"), "..-. .- .... -- .. | ..--- ----- ----- ..... ")

    def test_incorrect_user_input_e(characters):
        characters.assertEqual(PROJCODE.encryption("$%^&*@"), "######")

    def test_special_characters(characters):
        characters.assertEqual(PROJCODE.encryption("7 PERCENT %"), "--... | .--. . .-. -.-. . -. - | #")
        characters.assertEqual(PROJCODE.encryption("1 dollar $"), ".---- | -.. --- .-.. .-.. .- .-. | #")

    def test_case_sensitivity(characters):
        characters.assertEqual(PROJCODE.encryption("uppercase"), "..- .--. .--. . .-. -.-. .- ... . ")
        characters.assertEqual(PROJCODE.encryption("UppErCaSe"), "..- .--. .--. . .-. -.-. .- ... . ")
        
    def test_empty_string(characters):
        characters.assertEqual(PROJCODE.encryption(""), "")

    def test_phrase_inc_punctuation_e(characters):
        characters.assertEqual(PROJCODE.encryption("WHO, IS. THIS! MAN?"), ".-- .... --- --..-- | .. ... .-.-.- | - .... .. ... -.-.-- | -- .- -. ..--.. ")


#DECRYPTION CASES
     
    def test_decryption(characters):
        characters.assertEqual(PROJCODE.decryption(".- -... -.-."), "ABC")
        characters.assertEqual(PROJCODE.decryption(".- -... -.-. | ..--- ----- ----- ....."), "ABC 2005")

if __name__ == '__main__':
    unittest.main()
