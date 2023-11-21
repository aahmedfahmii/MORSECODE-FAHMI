#FIRST AND FOREMOST I AM CREATING A DICTIONARY THAT BASICALLY MAPS CHARACTERS (COULD BE LETTER,NUMBERS OR EVEN PUNCTUATION MARKS) TO THEIR INTERRELATED MORSE CODE REPRESENTATIONS.
#CURLY BRACES USED TO INITIALIZE AND DEFINE MY DICTIONARY  
my_dictionary = {                                        
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
'0': '-----', ' ': '|', ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--'
}

#DEFINING MY ENCRYPTION FUNCTION WHICH IS GOING TO TRANSLATE NORMAL ENGLISH LETTERS TO MORSE CODE

def encryption(word):

    morse_bank = []  #empty list to store user input

    index = 0
    
    while index < len(word):     # while loop iterating over all given letters
        
        letter = word[index].upper() # used upper method to change all given characters to uppercase
        
        if letter in my_dictionary:    
            morse_bank.append(my_dictionary[letter])     #if letter is in the morse dictionary it will add its morse representation to the empty list
            index += 1

        else:   
            morse_bank.append("#")     #application will return "#" for unknown characters
            index += 1

    return ''.join(morse_bank)    #join method used to bring the elements in the morse_bank list together without spaces


#DEFINING MY DECRYPTION FUNCTION WHICH IS GOING TO TRANSLATE MORSE CODE TO NORMAL ENGLISH LETTERS

def decryption(code):

    letter_bank = []

    code = code.split(' ')   #this 'split' method seperates the string at every ' ' character

    new_dict = {letter : morse for morse, letter in my_dictionary.items()}   #this is called reverse mapping which basically means it does the opposite mapping of "my_dictionary" making it easier to find letters for morse by switching the key and value
 
    for i in code:
        
        if i in new_dict:
            letter_bank.append(my_dictionary[i])

        elif i == ' ':
            letter_bank.append('|')       #if a space is given it will return '|' 

        else:   
            letter_bank.append("#")     #application will return "#" for unknown characters
    
    return ''.join(letter_bank)    #join method used to bring the elements in the letter_bank list together without anything between them which is represented by the empty string ('')