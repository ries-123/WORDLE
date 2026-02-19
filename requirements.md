Build a fully functional Wordle-style game using astronomy terms where players guess 5-letter space words with color-coded feedback. The challenge is implementing the game logic, managing word lists by difficulty, tracking player statistics, and providing educational value through each word revealed.

Students collect 5-letter astronomy terms (COMET, ORBIT, VENUS, QUARK, DWARF, TITAN) from astronomy glossaries and NASA resources, organizing them by difficulty level. The system uses string manipulation to validate guesses and check letter positions, stores game state in dictionaries (tracking which letters have been tried, their colors), implements NumPy arrays to track guess statistics and letter frequency analysis, and creates Matplotlib visualizations for win streaks and guess distributions. The LLM API generates contextual hints without giving away the answer, creates educational explanations after each word is revealed, and suggests related terms to expand vocabulary. Build a WordleGame class managing the game state with methods for checking guesses, implement file I/O to save daily words and player statistics, use try/except for handling invalid inputs, and apply control flow for the 6-guess limit and win conditions.

The minimal version uses a list of 30 astronomy words, implements the basic color logic (green for correct position, yellow for wrong position, gray for not in word), tracks guesses in a simple list, generates one hint via LLM after 3 failed attempts, and displays results with colored text output. Advanced versions might implement difficulty modes, create themed weeks, build a hard mode where revealed letters must be used, analyze which words are statistically hardest based on average guesses needed, generate custom word lists based on what students are currently studying, implement multiplayer battles with the same word, create a learning mode that teaches the term before the game, track letter position statistics to suggest optimal starting words, or build an infinite mode with increasingly obscure terms.


to do still:

- make an array with colored block symbols
- implements NumPy arrays to track guess statistics and letter frequency analysis
- The LLM API creates educational explanations after each word is revealed, and suggests related terms to expand vocabulary. 
- (?) Build a WordleGame class managing the game state with methods for checking guesses
- implement file I/O to save daily words and player statistics
- (?) apply control flow for the 6-guess limit and win conditions.
- 
