import pandas as pd
import requests
import io
import numpy as np

from Game import Game

if __name__ == '__main__':
    # loading the word bank
    url = 'https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt'
    download = requests.get(url).content

    # formatting the words array
    wordsdf = pd.read_csv(io.StringIO(download.decode('utf-8')), header = None).to_numpy()
    words = [word[0] for word in wordsdf]

    # playing the game
    game = Game(words)
    game.play()