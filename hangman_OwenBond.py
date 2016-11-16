#Owen Bond
#7th Period
#10/19/16


import random
import time
import os

def display_board(solved, guesses, strikes):
    if strikes == 0:
        print("""
_______
|/    |
|    
|      
|       
|      
|
|   """)
    if strikes == 1:
      print("""
_______
|/    |
|   (;_;)
|      
|       
|      
|
|    """)
    if strikes == 2:
        print("""
_______
|/    |
|   (;_;)
|     |
|     | 
|      
|
|          """)
    if strikes == 3:
        print("""
_______
|/    |
|   (;_;)
|    \\|
|     | 
|      
|
|          """)
    if strikes == 4:
        print("""
_______
|/    |
|   (;_;)
|    \\|/
|     | 
|      
|
|          """)
    if strikes == 5:
        print("""
_______
|/    |
|   (;_;)
|    \\|/
|     | 
|    / 
|
|          """)
    if strikes == 6:
        print("""
_______
|/    |
|   (;_;)
|    \\|/
|     | 
|    / \\
|
|          """)

    print(solved + " [" , strikes ,"]")
    print("You have already guessed: "+ guesses)
def show_start_screen():
    print("""
██╗     ███████╗████████╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗    
██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝    
██║     █████╗     ██║   ███████╗    ██████╔╝██║     ███████║ ╚████╔╝     
██║     ██╔══╝     ██║   ╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝      
███████╗███████╗   ██║   ███████║    ██║     ███████╗██║  ██║   ██║       
╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       
                                                                          
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██╗       
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║██║       
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║██║       
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║╚═╝       
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║██╗       
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝   """)
    
def show_credits():
    print("""
████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗    ███████╗ ██████╗ ██████╗     
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗    
   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗    █████╗  ██║   ██║██████╔╝    
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║    ██╔══╝  ██║   ██║██╔══██╗    
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║    ██║     ╚██████╔╝██║  ██║    
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝    
                                                                                    
██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗         ███╗ ██╗             
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝     ██╗██╔██╗╚██╗            
██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗    ╚═╝╚═╝╚═╝ ██║            
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║    ██╗       ██║            
██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    ╚═╝      ██╔╝            
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝              ╚═╝          """)

    print("")
    print("")
    print("")
    print("")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~                                                                                             ~")
    print("~                                                                                             ~")
    print("~                                        Made  by:                                            ~")
    print("~                                       Owain Bundi                                           ~")
    print("~                                                                                             ~")
    print("~                                                                                             ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for i in range(60):
        print("")
        time.sleep(.06)
    

def get_guess():
    guess = input("Guess a letter: ")
    guess = guess.lower()
    while True:
        
        if guess.isalpha() and len(guess) == 1:
            return guess
        guess = input("Make sure your guess is only one letter.  ")
        

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f
        with open(full_path, 'r') as file:
            print(str(i + 1) + ") " + file.readline().strip())
            

    choice = input("Enter selection: ")
    choice = int(choice) - 1

    
    return path + "/" + files[choice]

def get_puzzle(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:])

def confirm():
    pass

def play_again():
    response = input("Would you like to play again? (Yes / No)")
    response = response.lower()
    if response == 'yes':
        play()
    else:
        show_credits()
    pass

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    word = word.upper()

    solved = "-" * len(word)
    guesses = ""

    strikes = 0
    limit = 6

    solved = check(word, solved, guesses)
    
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()
        letter = letter.upper()

        if letter not in word and strikes < limit:
            strikes += 1
        
        guesses += letter
        
        solved = check(word, solved, guesses)

        display_board(solved, guesses, strikes)
    if word == solved:
        print("You win!")
    else:
        print("You lose!")
        print("The word was: "+ word)
    play_again()


def main():
    show_start_screen()
    play()
    

# code execution begins here
if __name__ == "__main__":
    main()
