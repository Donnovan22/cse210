class Jumper:
    def __init__(self):

        self._secret_word = ["_", "_", "_", "_", "_"]

        self._parachute = ["   _____   ",
                           "  /_____\  ",
                           "  \     /  ",
                           "   \   /   ",
                           "    \ /    "]
        self._toy = ["     O     ",
                     "    /|\    ",
                     "    / \    ", ]

    def displayParachuteAndPerson(self):
        print()
        print(
            f" {self._secret_word[0]} { self._secret_word[1]} {self._secret_word[2]} { self._secret_word[3]} {self._secret_word[4]}")
        print()
        for i in self._parachute:
            print(i)
        for j in self._toy:
            print(j)
        print()
        print(" ^^^^^^^^^")

    def set_parachute(self, index, value):
        self._parachute[index] = value

    def get_parachute(self):
        return self._parachute

    def set_toy(self, index, value):
        self._toy[index] = value

    def get_toy(self):
        return self._toy

    def set_secret_word(self, index, value):
        self._secret_word[index] = value

    def get_secret_word(self):
        return "".join(self._secret_word)
