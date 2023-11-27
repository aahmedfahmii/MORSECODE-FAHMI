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
            morse_bank.append(my_dictionary[letter] + ' ')     #if letter is in the morse dictionary it will add its morse representation to the empty list
            index += 1

        elif letter == ' ':
            morse_bank.append('|')     #if a space is given it will return '|'
             
        else:   
            morse_bank.append("#")     #application will return "#" for unknown characters
            index += 1

    return ''.join(morse_bank)    #join method used to bring the elements in the morse_bank list together without spaces


#DEFINING MY DECRYPTION FUNCTION WHICH IS GOING TO TRANSLATE MORSE CODE TO NORMAL ENGLISH LETTERS

def decryption(code):

    if '  ' in code:
        return('(ATTENTION: This is not your translation! Incorrect spacing detected. Please choose your programme again and re-enter your characters.)')
    
    letter_bank = []

    code = code.split(' ')   #this 'split' method seperates the string at every ' ' character

    new_dict = {letter : morse for morse, letter in my_dictionary.items()}   #this is called reverse mapping which basically means it does the opposite mapping of "my_dictionary" making it easier to find letters for morse by switching the key and value
 
    for i in code:
        
        if i in new_dict:
            letter_bank.append(new_dict[i])

        elif i == '|':
            letter_bank.append(' ')      

        else:   
            letter_bank.append("#")     #application will return "#" for unknown characters
    
    return ''.join(letter_bank)    #join method used to bring the elements in the letter_bank list together without anything between them which is represented by the empty string ('')

#DEFINING A FUNCTION TO RUN MY CODE, THIS FUNCTION COMPLETES MY APPLICATION WHERE IT ALLOWS THE USER TO CHOOSE OUT OF THREE OPTIONS (E,D,X)
#THE USER THEN INPUTS EITHER LETTERS OR MORSE CODE BASED ON HIS/HER CHOICE
#THE APPLICATION THEN TRANSLATES THE USER'S INPUT USING THE ENCRYPTION AND DECRYPTION FUNCTIONS

def start():

    name = input("PLEASE ENTER YOUR NAME: ")

    while True:                     #start an infinite loop to allow user to use the application multiple times until he/she decides to quit

        programme = input(
    '''CHOOSE PROGRAMME:
'E' : ENCRYPTION
'D' : DECRYPTION
'X' : EXIT
'''
).upper()               #changes any user input to capital letters to prevent from handling errors, ensures consistency and a more user friendly experience where it forgives regardless of capital or lower case input
        
        if programme == 'E':
            start_e = input(
                """WELCOME TO THE ENCRYPTION REALM, PLEASE ENTER YOUR LETTERS: 
note that '#' will be shown for unknown characters
"""
)
            print('ORIGINAL TEXT:' , start_e)
            print('MORSE CODE:' , encryption(start_e))
        elif programme == 'D':
            print("""PLEASE ENTER EACH LETTER'S MORSE CODE REPRESENTATION WITH EXACTLY 1 SPACE IN BETWEEN.
 (e.g. ABC = .- -... -.-. )
 note that '#' will be shown for unknown characters
 """
 )
            start_d = input("WELCOME TO THE DECRYPTION REALM, PLEASE ENTER YOUR MORSE CODE: ")
            print('ORIGINAL CODE:' , start_d)
            print('DECRYPTED TEXT:' , decryption(start_d))

        elif programme == 'X':
            print(f'THANK YOU {name.upper()} YOU HAVE SUCCESSFULLY ENDED YOUR SESSION')
            break

        else:
            print("UNKOWN PROGRAMME, PLEASE CHOOSE 'E FOR ENCRYPTION', 'D FOR DECRYPTION' OR 'X' TO EXIT")

if __name__ == '__main__':    #USED TO PREVENT THE UNITTESTING PART FROM RUNNING MY PROJCODE  TEXTFILE INSTEAD OF RUNNING ITS OWN CODE
    start()         #finally calling my start function to run my code and start my application
