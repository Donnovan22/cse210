class List:
    def __init__(self):
        self._wordList = []

    def _addWordsToWordList(self):
        with open("E:\Study\Programming with classes\cse210\week03\jumperGame\classes\words.txt") as listOfWords:
            for line in listOfWords:
                new_line = line.strip()
                self._wordList.append(new_line)

    def getWordList(self):
        self._addWordsToWordList()
        return self._wordList
