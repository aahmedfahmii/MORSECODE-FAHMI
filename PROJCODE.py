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

#DEFINING MY ENCRYPTION FUNCTION WHICH IS GOING TO TRANSLATE CODE FROM NORMAL ENGLISH LETTERS TO MORSE CODE

def encryption(word):

    morse_bank = []  #empty empty list to store user input
    
    for i in word.upper():      # used upper method to change all given characters to uppercase
                                #for loop iterates over all given letters
        if i in my_dictionary:     
            morse_bank.append(my_dictionary[i])     #if letter is in the morse dictionary it will add its morse representation to the empty list

        else:   
            morse_bank.append(" ")     #if the letter is not in the morse dictionary it will return nothing
    
    return (morse_bank)

