import random
from classes.wordList import List


class RandomWordGenerator:
    def __init__(self):
        self._wordList = List()
        self._myWordList = self._wordList.getWordList()

    def pickRandomWord(self):
        random_word = random.choice(self._myWordList)
        return random_word
