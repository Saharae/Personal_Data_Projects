from Board import Board
from collections import defaultdict

class Bucket:

    def __init__(self, words):
        '''
        Init for the Bucket class
        :param words: array or list of possible words to choose from
        '''
        self.valid_guesses = [w.upper() for w in words] # keeps them as strings
        self.possible_words = [Board(w) for w in words] # makes them Board instances
        self.guess = None
        self.bucket_counts = defaultdict(lambda: 0)
        self.target_status = None

    def size(self):
        '''
        Returns the number of words remaining in the bucket
        :return: number of words remaining
        '''
        return len(self.possible_words)

    def set_guess(self, guess):
        '''
        Checks the validity of a guess and saves it if it's valid
        :param guess: string guess for next round
        :return: True if valid, False otherwise
        '''
        if len(guess) != 5:
            print('Not a valid guess. The word must be 5 letters.')
            return False

        if guess.upper() not in self.valid_guesses:
            print('Not a valid guess. That word was not in the word bank. Please guess a valid word.')
            return False

        self.guess = Board(guess)
        return True

    def check_win(self):
        '''
        A win is if the current saved guess is the final word remaining in the bucket
        :return: True if a win, False otherwise
        '''
        return self.size() == 1 and self.guess.to_string() == self.possible_words[0].to_string()

    def set_counts(self):
        '''
        Determines the counts by possible resulting game state with the current guess.
        :return: None
        '''
        for word in self.possible_words:
            word.comp(self.guess)
            self.bucket_counts[word.status_str()] += 1

    def set_target_status(self):
        '''
        The resulting target status for the next round will have the largets number of resulting words left in the bucket.
        This target status is saved
        :return: None
        '''
        self.target_status = max(self.bucket_counts, key = self.bucket_counts.get)

    def narrow_bucket(self):
        '''
        Only words with the desired target status remain in the bucket
        :return: None
        '''
        narrow_words = [w for w in self.possible_words if w.status_str() == self.target_status]
        self.possible_words = narrow_words
        self.bucket_counts = defaultdict(lambda: 0)

    def get_winner(self):
        '''
        Returns first word in the bucket. If there's more than one word left it will say so, but that shouldn't happen
        :return: first (hopefully only) word left in the bucket
        '''
        if self.size() != 1:
            print('The game is not won. But heres the first word.')
        return self.possible_words[0]

    def cycle(self):
        '''
        algorithm cycle of counting possible bucket sizes, choosing the largest, and narrowing the bucket
        :return:
        '''
        self.set_counts()
        self.set_target_status()
        self.narrow_bucket()
