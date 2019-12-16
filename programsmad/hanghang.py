import sys
from termcolor import colored, cprint
import time
import random

#Hangman


#Scaffold printouts
scaffold = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
       "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
       "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
       "_______\n|     |\n|\n|\n|\n|\n|\n=======",
      ]
           
#List of Capitals from files...
def obtain_list():
    lista = []
    with open('countries_and_capitals.txt', 'r') as myFile:
        hangList = list(myFile)
        hangList[182] += 'e'
        for pereche in hangList:
            pereche = pereche[:-1]
            separate = pereche.split(' | ')
            if ' ' in separate[1]:
                z = separate[1].split()
                separate[1] = ''.join(z)
            lista.append(separate)
    return lista
#Make 3 levels of difficulty
easy_letters = []
medium_letters = []
hard_letters = []
x = obtain_list()
lungimeX = len(x)
for i in range(0, lungimeX):
    if len(x[i][1]) < 6:
        easy_letters.append(x[i][1].upper())
    elif len(x[i][1]) < 10:
        medium_letters.append(x[i][1].upper())
    else:
        hard_letters.append(x[i][1].upper())
        
#Program Functions
def pick_diff():
    """Let the player pick and confirm a difficulty level."""
    prompt = "Pick a difficulty, please. (Easy, Medium, Hard)\n>"
    choice = ""
    while choice not in ['easy', 'medium', 'hard']:
        choice = input(prompt)
        choice = choice.lower()
    change_diff(choice)

def change_diff(level):
    """Allow the player a chance to change difficulty."""
    message = "\nYou picked " + level + ". Do you want to change it? [Y/N]\n>"
    answer = ""
    while answer not in ['y', 'n']:
        answer = input(message)
        answer = answer.lower()
    if answer == 'y':
        pick_diff()
    if answer == 'n':
        print("\nLET'S PLAY!\n")
        choose_word(level)
#Make stop watch     
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lasped = {0} hours: {1} minutes: {2:d} seconds".format(int(hours), int(mins), int(sec)))

def choose_word(choice):
    """Assign the game word based on player difficulty choice."""
    if choice == 'easy':
        word = random.choice(easy_letters)
    elif choice == 'medium':
        word = random.choice(medium_letters)
    elif choice == 'hard':
        word = random.choice(hard_letters)
    cuvant = list(word)
    lungime = len(cuvant)
    for k in range(0, lungime):
        cuvant[k] = cuvant[k] + ' '
    word = cuvant
    play_game(word)

def play_game(this_word):
    """Run the actual game of hangman."""
    start_time = time.time()
    word = list(this_word)
  
    blanks = list()
    for i in range (0, len(word)):
        blanks.append("_ ")
    guessed = []
    incorrect = 6
    while incorrect > 0:
        text = colored('', 'yellow', attrs=['blink'])
        print(text) 
        cprint("\n" + scaffold[incorrect]
              + "\nYou have {} life points left.".format(incorrect)
              + "\nYour word: " + "".join(blanks)
              + "\nGuessed letters: " + ", ".join(guessed), 'yellow')
        #Help for player with country name
        if incorrect == 1:
            temp = []
            for u in range(0, len(word)):
                temp.append(word[u].strip()) 
            checkWord = ''
            checkWord = ''.join(temp).lower().capitalize()
            for t in range(0, lungimeX):
                if checkWord == x[t][1]:
                    print(f'The capital of {x[t][0]}')
        #Check player input       
        letter = input("Your guess: ").upper()
        if len(letter) == 1 and letter.isalpha():
            letter += " "
            if letter in guessed:
                print("\n\nYou already guessed that!")
            elif letter in word:
                for index,character in enumerate(word):
                    blanks = list(blanks)
                    if character == letter:
                        blanks[index] = letter
                        "".join(blanks)
                        if blanks == word:
                            text = colored(' ', 'cyan', attrs=['blink'])
                            print(text)   
                            cprint("\n\nCONGRATULATIONS,you are the winner! And our world is safe ! :)\nYour word was " + ''.join(word) + ".\n", 'cyan')
                            end_time = time.time()
                            time_lapsed = end_time - start_time
                            time_convert(time_lapsed)
                            play_again()
            elif letter not in word:
                incorrect -= 1
                guessed.append(letter)
        else:
            print("\n\n!Only single letters allowed!\n\n")
    else:
        print(scaffold[0])
        text = colored(' ', 'red', attrs=['blink'])
        print(text) 
        cprint("\nSorry " + player + ", your game is over!\nYour word was " + ''.join(word) + ".", 'red')
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)
        play_again()

def play_again():
    """Offer the player a chance to play again."""
    repeat = input("Would you like to play again " + player + "? [Y/N]\n>").lower()
    if repeat == 'y':
        print("Let's play!")
        pick_diff()
    else:
        text = colored(' ', 'red', attrs=['bold'])
        print(text) 
        cprint("Thanks for playing! Have a great day!", 'red')
        sys.exit()

# Welcome the player, get their name and explain the game.
player = input("Let's play hangman! Please type your name.\n>").lower()
player = player.title()
print("\nHey, " + player + "!\nYou get six lives before you lose.\nYou have to guess a capital city name to win the game!.\nWhich difficulty would you like?\n  Easy \n  Medium \n  Hard ")

# Select the difficulty and begin the game
pick_diff()