
from game.card import Card


class Game:

    def __init__(self):
        self.value = 300
        self.is_playing = True
        self.card1_value = 0
        self.card2_value = 0
        self.option = ""
        self.user = ""

    def startGame(self):
        print("\nWelcome to HILO GAME !!!")

        while self.is_playing:
            self.card1 = Card()
            self.card1.roll()
            self.card1_value = self.card1.value

            self.card2 = Card()
            self.card2.roll()
            self.card2_value = self.card2.value

            self.printMessages()
            self.getInputs()
            self.calculatePoints()

            if self.playAgain() == "n":
                print("\nThanks For Playing")
                self.is_playing = False
            if self.value <= 0:
                print(f"\nYou scored {self.value} Game is over!!!")
                self.is_playing = False

    def getInputs(self):
        user_guess = input("Higher or Lower? [h/l]: ")
        self.user = user_guess

    def calculatePoints(self):

        print(f"Next Card was: {self.card2_value}")
        if self.card1_value > self.card2_value:
            self.option = "l"
        elif self.card1_value < self.card2_value:
            self.option = "h"
        elif self.card1_value == self.card2_value:
            self.value = self.value

        if self.option == self.user:
            self.value += 100
        if self.option != self.user:
            self.value -= 75

        print(f"Your Score is: {self.value}")

    def printMessages(self):
        print(f"\nThe Card is: {self.card1_value}")

    def playAgain(self):
        userChoice = input("Play again? (y/n): ")
        return userChoice
