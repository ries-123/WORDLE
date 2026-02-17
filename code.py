##saving progress: git add ____, git commit -m "message", git push origin main

## importing ts
import numpy as np
import random
import matplotlib.pyplot as plt

## list of words
astro_words = [
    "Space", "Earth", "Lunar", "Solar",
    "Orbit", "Light", "Night", "Comet", 
    "Radio", "Pluto", "Alpha", "Venus",
    "Phase", "Flare",
    "Mount", "Aries", "Dwarf", "Orion",
    "Titan", "Bulge", "Libra", "Virgo",
    "Epoch", "Thebe", "Ceres", "Umbra", 
    "Helix", "Deneb", "Nadir", "Apsis",
    ]
## word selection moved after difficulty
guesses_left = 6
guesses_so_far = 0 # guesses # so far, will be printed after each guess
appended_guess = [] #list of guesses, will be printed after each guess
n = 0 #this is the thing that will count up to test each letter (see below)
appended_letters = [] #list of letters guessed so far
guessed_letter_colors = {} # maps letter to its most recent color code
colored_letters = [] #list of letters with colors, will be printed after each guess
##print(word, word_letters) ##remove this l8r(test)

#variables
guess_on_one = 0 
guess_on_two = 0
guess_on_three = 0 
guess_on_four = 0 
guess_on_five = 0
guess_on_six = 0 
loss_counter = 0
play = "yes"

print("AstWordle: Astronomy meets Wordle. ")
#game loop
while play=="yes":
    while True:  
        difficulty = input("choose your difficulty: easy, hard or ULTRAkill!!!: ").lower()
        if difficulty == "easy":
            astro_words_difficulty = astro_words[0:9]
            break
        elif difficulty == "hard":
            astro_words_difficulty = astro_words[10:19]
            break
        elif difficulty == "ultrakill":
            astro_words_difficulty = astro_words[20:29]
            break
        else:
            print("Please enter easy, hard, or ultrakill.")
    # Now select the word from the correct difficulty
    word = random.choice(astro_words_difficulty).upper()
    word_letters = list(word)
    print("you have 6 tries. after 3, you will be offered a hint.")
    ##loops until user imputs the right type of stuff

    while guesses_left > 0: #later add a nested thing where api gives hint if guesses_left == 3
        while True:
            guess = input("Enter a 5-letter word: ").upper()
            if len(guess) != 5:
                print("Please enter exactly 5 letters.")
                continue
            if not guess.isalpha():
                print("Please enter only letters.")
                continue
            break


#win conditions, helps keep track of wins per guess stats
        if guess == word and guesses_so_far == 0:
            guess_on_one += 1
            print(f"congratulations you did it!! the word was {word}. you guessed it on guess #{guesses_so_far + 1}")
            break
        elif guess == word and guesses_so_far == 1:
            guess_on_two += 1
            print(f"congratulations you did it!! the word was {word}. you guessed it on guess #{guesses_so_far + 1}")
            break
        elif guess == word and guesses_so_far == 2:
            guess_on_three += 1
            print(f"congratulations you did it!! the word was {word}. you guessed it on guess #{guesses_so_far + 1}")
            break
        elif guess == word and guesses_so_far == 3:
            guess_on_four += 1
            print(f"congratulations you did it!! the word was {word}. you guessed it on guess #{guesses_so_far + 1}")
            break
        elif guess == word and guesses_so_far == 4:
            guess_on_five += 1
            print(f"congratulations you did it!! the word was {word}. you guessed it on guess #{guesses_so_far + 1}")
            break
        elif guess == word and guesses_so_far == 5:
            guess_on_six += 1
            print(f"congratulations you did it!! the word was {word}. you guessed it on guess #{guesses_so_far + 1}")
            break

        
    
        # appended_guess.append(guess) #makes list of guesses so far
        
        guess_letters = list(guess) #turns guess into letters, separates them into diff strings to test
        

        for n in range(5):
            letter = guess_letters[n]
            # Determine color code for this letter in this guess
            if guess_letters[n] == word_letters[n]:
                color = '\x1b[102m'  # green
                colored_letters.append(f"\x1b[102m{letter}\x1b[0m")
                print(f"in {guess}, \x1b[102m{letter}\x1b[0m is correct and in the right position")
            elif letter in word_letters:
                color = '\x1b[103m'  # yellow
                colored_letters.append(f"\x1b[103m{letter}\x1b[0m")
                print(f"in {guess}, \x1b[103m{letter}\x1b[0m is correct but in the wrong position")
            elif letter not in word_letters:
                color = '\x1b[100m'  # gray
                colored_letters.append(f"\x1b[100m{letter}\x1b[0m")
                print(f"in {guess}, \x1b[100m{letter}\x1b[0m is not in the word")
            else:
                color = ''
            # Always update the color for the letter to the most recent
            guessed_letter_colors[letter] = color
            if letter not in appended_letters:
                appended_letters.append(letter)

        # Print colored guess for this round
        ("".join(colored_letters))
        n = 0

        guesses_left -= 1
        guesses_so_far += 1


        # Print all unique letters guessed so far (sorted, with color)
        print("letters guessed so far:")
        sorted_letters = sorted(appended_letters)
        colored_guessed = [f"{guessed_letter_colors[l]}{l}\x1b[0m" for l in sorted_letters]
        print(" ".join(colored_guessed))
        print(f"you have {guesses_left} guesses left")

        if guesses_left <= 0:
            print(f"\x1b[31m*extremely loud incorrect buzzer*\x1b[0m] nah bru it was {word}")
            loss_counter += 1
            break

        
    
    print({guess_on_one}, {guess_on_two}, {guess_on_three}, {guess_on_four}, {guess_on_five}, {guess_on_six})
    guess_graph_x = ['1', '2', '3', '4', '5', '6'] #x axis for graph, will be used to show how many guesses it took to win
    guess_graph_y = [guess_on_one, guess_on_two, guess_on_three, guess_on_four, guess_on_five, guess_on_six] 
    plt.bar(guess_graph_x, guess_graph_y, color='light_green') #makes the graph
    plt.xlabel('Guess Number') #x axis label    
    plt.ylabel('Number of Wins') #y axis label
    plt.title("AstWordle Guess Distribution") #title of graph
    plt.show() #shows the graph

    #asking user to play again
    while True:
        play=input("play again? yes/no: ").lower()
        if not play == "yes" or play == "no":
            print("Please enter yes or no.")
            continue
        break


    



