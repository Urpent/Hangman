import random
from time import sleep

#-----------------------------------------------------------
#-------------------------Constants-------------------------
#-----------------------------------------------------------


#Variable name must match topic list element name Eg. 'musical instruments' -> musicalinstrument
topics = ('fruits', 'sports', 'superheroes','movies', 'musical instruments') #Small letter

#Fruits & Hint List
fruits = ('watermelon', 'orange', 'banana') 
watermelon_hint =("It's Round!", 'It Contains 94% water')
orange_hint = ('High Vitamin C','Its name is similar to a colour')
banana_hint = ('Lots of fiber','Yellow')

#Sports & Hint List
sports = ('basketball','swimming','badminton')
basketball_hint = ('Ten playes team game','Dunking!')
swimming_hint = ('Water Sport','start with "S"')
badminton_hint = ('Two or Four players game','Racket')

#SuperHeroes & Hint List
superheroes = ('professor x','wolverine','gambit')
professorx_hint = ('Mind control','Smart')
wolverine_hint = ('Super regeneration','Has Claw!')
gambit_hint = ('Throw card','Has a Pole')

#Movies & Hint List
movies = ('inception','the lord of the rings', 'the core')
inception_hint = ( 'Reality and Dream','Released on 2010')
thelordoftherings_hint = ('Orc','Drawf!')
thecore_hint = ('Deep inside the earth','Hot')

#Musical Instrument & Hint List
musicalinstruments = ('cello','bass guitar','piano')
cello_hint = ('Strings','Big!')
bassguitar_hint = ('Low','Strings')
piano_hint = ('Lots of Keys','Pedals')


#-----------------------------------------------------------
#--------------------------Methods--------------------------
#-----------------------------------------------------------

def sdisplay(message): #Special Display - letter by letter
    for x in message:
        print(x,end='')
        sleep(0.01)
    print('\n')

        
def display_topic_for_selection():  #Prompt user for input
    global topics

    print('\nPick a Topic\n')
    for x in range(len(topics)):
        sdisplay("       {} : {}".format(x, topics[x].title()))
    sdisplay("       q : Quit")
    
    while 1:
        selected_topic = input("\nEnter Topic's Number > ")
        if selected_topic =='q' or selected_topic.isdigit() and int(selected_topic) <= len(topics):   
            return selected_topic
        else:
            print('Invalid Topic, Try Again!')

        
def display_correct_word(word): #Display dashes line or letter for correctly guessed word
    print("\nWord: ", end ='')
    for letter in word:
        if letter:
            if letter == ' ':
                print('  ', end='')
            else:
                print(letter.upper() + ' ', end='')
        else:            
            print('_' + ' ', end='')
    print()


def get_valid_guess(correct_letters, missed_letters): #Loop till user give valid letter
    while 1:
        letter = input('Guess: ')
        if not letter.isdigit() and len(letter) == 1: #Condition - One letter only
            if letter in correct_letters or letter in missed_letters:
                print('You already guessed that letter')
            else:          
                break
        else:
            print('Invalid letter, try again!')
    return letter.lower()


def is_correct(guessed_letter): #Update tracking list and return True if letter is correctly guessed
    if guessed_letter in word:
        for i in range(len(word)):
            if word[i] == guessed_letter:
                correct_letters[i] = guessed_letter
        return True
    else:
        missed_letters.append(guessed_letter)
        missed_letters.sort()
        return False

    
def display_hangman(level): #Print hangman picture
    if level ==0:
        print('  |\n  |\n  |\n  |\n _|_')
    elif level == 1:
        print('   ___\n  |   |\n  |\n  |\n  |\n _|_')
    elif level == 2:
        print('   ___\n  |   |\n  |   O\n  |\n  |\n _|_')
    elif level == 3:
        print('   ___\n  |   |\n  |   O\n  |   |\n  |\n _|_')
    elif level == 4:
        print('   ___\n  |   |\n  |   O\n  |  /|\n  |\n _|_')
    elif level == 5:
        print('   ___\n  |   |\n  |   O\n  |  /|\ \n  |\n _|_')
    elif level == 6:
        print('   ___\n  |   |\n  |   O\n  |  /|\ \n  |  /\n _|_')
    else:
        print('   ___\n  |   |\n  |   O\n  |  /|\ \n  |  / \ \n _|_')



    
#----------------------------------------------------------- 
#---------------------------Main----------------------------
#-----------------------------------------------------------

print('**HANGMAN**')
display_hangman(7)
#   ___
#  |   |
#  |   O
#  |  /|\
#  |  / \
# _|_



selected_topic = ''
while selected_topic != 'q': #for quitting game
    
    selected_topic = display_topic_for_selection() #Get valid topic input from user
    if selected_topic =='q': #Quit if user enter 'q'
        print('Exited')
        continue
    
    words = eval(topics[int(selected_topic)].replace(' ','')) #Get list of words of the topic
    word = random.choice(words)               #Get random word from selected topic
    hint_list = eval(word.replace(' ','') + "_hint")       #Get Hint List from selected word

    
    missed_letters = []                              #For keeping track of wrongly guessed letters
    correct_letters = ['' for x in range(len(word))] #For keeping track of correctly guessed letters

    
    for i in range(len(word)): #Correct whitespace
        if word[i] == ' ':
            correct_letters[i] = ' '
    
    win = False
    while len(missed_letters) <7: #Allow user to make six guesses
        
        print()
        display_hangman(len(missed_letters))
        display_correct_word(correct_letters) #Show correctly guess number
        print('Misses:',','.join(missed_letters)) #Show wrongly guessed number
        guessed_letter = get_valid_guess(correct_letters, missed_letters) #Get letter from user
    
        if is_correct(guessed_letter): #Check if user won the game
            if '' not in correct_letters: 
                win = True
                break #break loop when user won
        elif len(missed_letters) >1: #Give hint when user missed more than 2 times
            print("Hint:",random.choice(hint_list))

    if win:
        display_correct_word(correct_letters) #Show correctly guess number
        sdisplay('\n\nGuesser Win!')            
    else:
        display_hangman(7) #Show dead hangman if lose
        sdisplay('\n\nGuesser loses - the answer was {}\n\n'.format( word.upper()))   
        print('\n')


        


