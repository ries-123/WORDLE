this is the psudocode for our astro wordle game
.------------------------------------------------.
create a list of 30 5-letter astro terms
add numpy
(for everything add .upper to make everything uppercase just in case the user uses mixed caps)
pick random word from list (do not tell user)
split the letters of the word into separate variables (list)
prompt the user for a 5 letter word
if they give non 5 letter word ask again
split the user's imput into letters as well (list)
test to see if the first letter of the user's imput matches the first letter of the bot's word
{if it is, indicate that (make it green or sum)
if its not, check if the user's first letter is equal to any of the other letters of the chosen word}
repeat ^the above^ for the other letters
