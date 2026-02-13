##saving progress: git add ____, git commit -m "message", git push origin main

## importing ts
import numpy as np
import random

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

## variables
word = random.choice(astro_words).upper()
word_letters = list(word)
guesses_left = 6
appended_guess = []
n = 0 #this is the thing that will count up to test each letter (see below)

##print(word, word_letters) ##remove this l8r(test)

##loops until user imputs the right type of stuff
print("AstWordle: Astronomy meets Wordle. you have 6 tries to guess a 5 letter word")
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
    if guess == word:
        print(f"congratulations you did it!! the word was {word}")
        break
   
    appended_guess.append(guess) #makes list of guesses so far
    print(f"so far you have guessed: {appended_guess}, you have {guesses_left} guesses left") 
    guess_letters = list(guess) #turns guess into letters, separates them into diff strings to test
    
    for n in range(5): #tests each letter in the guess, n is the thing that counts up to test each letter
        
        if guess_letters[n] == word_letters[n]: #if the two first letters are the same
            print(f"in {guess}, {guess_letters[n]} is correct and in the right position")
        elif guess_letters[n] in word_letters:
            print(f"in {guess}, {guess_letters[n]} is correct but in the wrong position")
        else:
            print(f"in {guess}, {guess_letters[n]} is not in the word")
        n += 1 #adds 1 to n so it can test the next letter in the next loop
            
    n = 0 #resets n to 1 so it can test the next guess
    guesses_left -= 1 #subtracts 1 from # of guesses left
    if guesses_left <= 0:
        print(f"*extremely loud incorrect buzzer* nah bru it was {word}")
        break
    



