
# WORDLE Variation Replication

----

Replication of Absurdle, an adversarial Wordle variation.
All credit and rights to the game belong to the original creator of Absurdle,
found at this link: https://qntm.org/files/absurdle/absurdle.html.

This is not a graphical game, but a text implementation played in the command line.
The class set up allows for expansion, so visualization can be added at a later date.

## Files

----

**main.py** -- main function to play the game

**Game.py** -- Game class that runs the game loop and keeps track of the score.

**Bucket.py** -- Bucket class that keeps track of the possible words, the current guess,
the game state, and runs the adversarial algorithm.

**Board.py** -- Board class that keeps track of a single word instance. Performs the checks
agains the guesses and determines the resulting state.


## To Run

----

`python3 main.py` will run the code in the command line

## To Play

----

This is an adversarial, command line, Wordle. The object of the game is to narrow the computer into a 
"chosen word" that you guess, in as few rounds as possible. I would suggest reading the official Absurdle
documentation, as the description and explanation is very clear.

Because this is currently a command line implementation, there are no graphics to assist you.
Instead there is a "Pattern" that gets printed every round. The pattern will be a string of 5 numbers
that correspond with the Wordle colors.

**0** = grey = that letter is not in the word  
**1** = yellow = that letter is in the word in a different spot  
**2** = green = that letter is in the correct spot in the word  

If you guess "START" and the resulting pattern is "00210" then you know the 'A' is in the correct spot,
 there is an 'R' in the word in a different spot, and there is no 'S' or 'T' in the word at all.

Because there is no keyboard you will have to keep track of the remaining letters on your own for now.


## Notes on the word bank

----

The chosen word bank is not the same as the word bank for Wordle or Absurdle.
This was done because I did not want to risk spoiling the daily word game for myself
by seeing the possible solutions.

Given this, the mechanics are slightly different, the word bank and the possible guesses
are the same group of words. As such, it will not function the exact same as Absurdle does.

If you want to pass it a different word bank, the only file that will need to be edited is the
*main.py* file. The Game class takes in a word bank as its only parameter, changing this will 
change the possible words and the solutions.