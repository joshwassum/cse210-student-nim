import random

class Board:

    def __init__(self):
        self._piles = []
        self._prepare()
        print("Hello World")

    def apply(self, move):
        print("Pile " + str(move._pile))
        print("Stones " + str(move._stones))
        self._piles[move._pile] -= move._stones
        print(self._piles)

    def is_empty(self):
        if sum(self._piles) == 0:
            return True
        else:
            return False

    def to_string(self):
        board ="---------------\n"
        for i in range(0, len(self._piles)):
            board += str(i) + ": "
            if self._piles[i] == 9:
                board += "O O O O O O O O O\n"
            elif self._piles[i] == 8:
                board += "O O O O O O O O\n"
            elif self._piles[i] == 7:
                board += "O O O O O O O\n"
            elif self._piles[i] == 6:
                board += "O O O O O O\n"
            elif self._piles[i] == 5:
                board += "O O O O O\n"
            elif self._piles[i] == 4:
                board += "O O O O\n"
            elif self._piles[i] == 3:
                board += "O O O\n"
            elif self._piles[i] == 2:
                board += "O O\n"
            elif self._piles[i] == 1:
                board += "O\n"
            else:
                board += "\n"
        board +="---------------"
        return board


    def _prepare(self):
        for i in range(0, random.randint(2,5)):
            self._piles.append(random.randint(1, 9))