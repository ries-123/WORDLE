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
    guesses_left -= 1
    print(f"you guessed: {guess}")
    user_letters = list(guess)
    #print(user_letters)
    if guesses_left == 0:
        print(f"*extremely loud incorrect buzzer* nah bru it was {word}")
        break