
from classes.jumper import Jumper
from classes.randomWord import RandomWordGenerator


class Game:
    def __init__(self):
        self._secretWord = RandomWordGenerator()
        self._jumper = Jumper()
        self._is_playing = True
        self._secret_word = self._secretWord.pickRandomWord()
        self._list_of_letters = list(self._secret_word)
        self._my_letter = ""
        self._guess_letters = []

    def start_game(self):
        print("\n!!!Welcome to Jumper Game!!!")

        while self._is_playing:

            self._jumper.displayParachuteAndPerson()
            self._get_input()
            self._compute_logic()
            self._check_status()

        self._jumper.displayParachuteAndPerson()
        print("Game is Over")
        print("Thanks for playing")

    def _get_input(self):
        letter = input("Guess a letter [a-z]: ")
        self._guess_letters.append(letter)
        self._my_letter = letter

    def _compute_logic(self):
        if self._my_letter in self._list_of_letters:
            index = self._list_of_letters.index(self._my_letter)
            self._jumper.set_secret_word(index, self._my_letter)
        else:
            try:
                self._jumper.get_parachute().pop(0)
            except:
                self._jumper.set_toy(0, "     X")
                self._is_playing = False

    def _check_status(self):
        string = self._jumper.get_secret_word()
        if string == self._secret_word:
            self._is_playing = False
