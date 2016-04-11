import random


class Dice:

    def __init__(self):
        self.value = None

    def throw(self):
        self.value = random.randint(1, 6)


class Player:

    def __init__(self, name):
        self.name = name
        self.diceA = Dice()
        self.diceB = Dice()
        self.score = 0

    def turn(self):
        # Cast dices
        self.diceA.throw()
        self.diceB.throw()

        if self.diceA.value == self.diceB.value:
            self.doubles()

    def doubles(self):
        if self.diceA.value == 3:
            self.score = 0
        else:
            self.good_double()

    def good_double(self):
        if self.diceA == 6:
            self.score += 25
        else:
            self.score += 5


class Fifty:

    def __init__(self):
        # Set the two scores to zero
        self.player_1 = Player("Vesa")
        self.player_2 = Player("John")
        self.threshold = 50

    def play(self):

        while self.player_1.score < self.threshold and self.player_2.score < self.threshold:
            self.player_1.turn()
            self.player_2.turn()

    def evaluate(self):
        if self.player_1.score == self.player_2.score:
            return "Tie"
        else:
            if self.player_1.score > self.player_2.score:
                return self.player_1.name
            else:
                return self.player_2.name

if __name__ == "__main__":

    game = Fifty()
    game.play()
    print(game.evaluate())
