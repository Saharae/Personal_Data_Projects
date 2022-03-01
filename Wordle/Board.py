import numpy as np
class Board:
    def __init__(self, word):
        '''
        Takes in a single word to be turned into a game state
        :param word: string word
        '''
        self.word = np.array(list(word))
        self.word = [w.upper() for w in self.word]
        self.guess = None
        self.win = False
        self.status = [None, None, None, None, None]

    def comp(self, guess):
        '''
        Compares a guess to the current word and sets the status. 0 = not in word. 1 = in word in wrong place. 2 = in right place
        :param guess: another Board instance.
        :return: self. the original word.
        '''
        self.guess = guess
        for i in range(5):
            if guess.word[i] == self.word[i]:
                self.status[i] = 2
            elif guess.word[i] in self.word:
                self.status[i] = 1
            else:
                self.status[i] = 0
        return self

    def status_str(self):
        '''
        Joins the status array into single string for printing
        :return: status string
        '''
        s = ''.join([str(a) for a in self.status])
        return s

    def to_string(self):
        '''
        Joins array form of word back into a string for printing
        :return: string of word
        '''
        return ''.join(self.word)

    def __repr__(self):
        return self.to_string()
