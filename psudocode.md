    this is the psudocode for our astro wordle game
    .------------------------------------------------.
    create a list of 30 5-letter astro terms
    add numpy
    (for everything add .upper to make everything uppercase just in case the user uses mixed caps).
    pick random word from list (do not tell user).
    split the letters of the word into separate variables (list). 
    prompt the user for a 5 letter word. 
    if they give non 5 letter word ask again. 
    if the user gives anything other than pure letters prompt again
    split the user's imput into letters as well (list). 
    test to see if the first letter of the user's imput matches the first letter of the bot's word. 
    {if it is, indicate that (make it green or sum). 
    if its not, check if the user's first letter is equal to any of the other letters of the chosen word}. 
    if not, make letter grey. 
    repeat ^the above^ for the other letters. 
    track which letters have been tried and their colors in dictionaries.(list prev word guesses and the colors of the letters, 
        maybe have the whole alphabet displayed that also changes color accordingly). 
    allow player to guess 5 more times (total of 6). 
    "implement NumPy arrays to track guess statistics and letter frequency analysis"(? ig bro). 
    make wins graph - shows how many times a player has won with each amount of guesses. 
    have LLM API generate hint (after 3 failed attempts) 
    explain the word in the context of astronomy. 


