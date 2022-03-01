from Bucket import Bucket

class Game:
    def __init__(self, wordbank):
        self.wordbank = wordbank
        self.word_bucket = Bucket(self.wordbank)
        self.WON = False
        self.count = 0

    def play(self):
        # Game loop. Will end when the player guesses the only word left, or leaves the game with only 1 option left.
        while not self.WON:

            valid = self.word_bucket.set_guess(input("Guess?: "))

            while not valid: # a valid guess has only 5 letters and is in the passed word bank
                valid = self.word_bucket.set_guess(input("Guess?: "))

            # checks the win condition
            if self.word_bucket.check_win():
                self.WON = True
                print('You won. Nice going! The word was: ', self.word_bucket.get_winner())
                print(f'It took you {self.count} guesses to win')
                break

            # if the game is not won it runs through the cycle of narrowing the bucket of possible words
            self.word_bucket.cycle()

            # round count increase
            self.count += 1

            # checks for a second win condition of the word not being the last one left in the round start, but being the only one left at the end
            if self.word_bucket.check_win():
                self.WON = True
                print('You won. Nice going! The word was: ', self.word_bucket.get_winner())
                print(f'It took you {self.count} guesses to win')

            # prints the pattern for the next round
            print("PATTERN: ", self.word_bucket.target_status)







