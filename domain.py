from random import randint

class Square:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y


class Board():
    def __init__(self, inpt):
        self.__inpt = inpt
        self.__b = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # self.__b = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

        # self.__b = [[0]*inpt]*inpt
        # print(self.__b)

    def isFree(self, l, c):
        if self.__b[l][c] == 0:
            if l == 0 and c == 0:
                if self.__b[l + 1][c] == 0 and self.__b[l + 1][c + 1] == 0 and self.__b[l][c + 1] == 0:
                    return True
                return False
            if l == self.__inpt - 1 and c == self.__inpt - 1:
                if self.__b[l - 1][c] == 0 and self.__b[l - 1][c - 1] == 0 and self.__b[l][c - 1] == 0:
                    return True
                return False
            if l == 0 and c == self.__inpt - 1:
                if self.__b[l][c - 1] == 0 and self.__b[l + 1][c] == 0 and self.__b[l + 1][c - 1] == 0:
                    return True
                return False
            if l == self.__inpt - 1 and c == 0:
                if self.__b[l - 1][c] == 0 and self.__b[l][c + 1] == 0 and self.__b[l - 1][c + 1] == 0:
                    return True
                return False
            if l == 0:
                if self.__b[l][c - 1] == 0 and self.__b[l][c + 1] == 0 and self.__b[l + 1][c + 1] == 0 and \
                        self.__b[l + 1][c - 1] == 0 and self.__b[l + 1][c] == 0:
                    return True
                return False
            if l == self.__inpt - 1:
                if self.__b[l][c - 1] == 0 and self.__b[l][c + 1] == 0 and self.__b[l - 1][c] == 0 and self.__b[l - 1][
                    c - 1] == 0 and self.__b[l - 1][c + 1] == 0:
                    return True
                return False
            if c == 0:
                if self.__b[l + 1][c] == 0 and self.__b[l - 1][c] == 0 and self.__b[l][c + 1] == 0 and self.__b[l + 1][
                    c + 1] == 0 and self.__b[l - 1][c + 1] == 0:
                    return True
                return False
            if c == self.__inpt - 1:
                if self.__b[l + 1][c] == 0 and self.__b[l - 1][c] == 0 and self.__b[l][c - 1] == 0 and self.__b[l - 1][
                    c - 1] == 0 and self.__b[l + 1][c - 1] == 0:
                    return True
                return False
            if self.__b[l - 1][c] == 0 and self.__b[l + 1][c] == 0 and self.__b[l][c - 1] == 0 and self.__b[l][
                c + 1] == 0 and self.__b[l - 1][c + 1] == 0 and self.__b[l - 1][c - 1] == 0 and self.__b[l + 1][
                c - 1] == 0 and self.__b[l + 1][c + 1] == 0:
                return True
            return False
        else:
            return False

    def getFreeSquares(self):
        rez = []
        for i in range(0, self.__inpt):
            for j in range(0, self.__inpt):
                if self.isFree(i, j) == True:
                    rez.append(Square(i, j))
        return rez

    def isFull(self):
        return len(self.getFreeSquares()) == 0

    def getAll(self):
        return self.__b

    def __str__(self):
        list = self.getAll()
        string = '   '
        for i in range(0, self.__inpt):
            string = string + str(i) + " "
        string = string + '\n'
        for i in range(0, self.__inpt):
            string = string + str(i) + ": "
            for j in range(0, self.__inpt):
                string = string + str(list[i][j]) + ' '
            string = string + '\n'
        return string

    def play(self, l, c, player):
        if l < 0 or l > self.__inpt - 1 or c < 0 or c > self.__inpt - 1:
            raise Exception("Bad coordonates! \n")
        if player not in ['y', 'x']:
            raise Exception("Bad player! \n")
        if self.isFree(l, c) == False:
            raise Exception("Bad position! \n")
        self.__b[l][c] = player


class Game():
    def __init__(self, inpt):
        self.__inpt = inpt
        self.__board = Board(inpt)

    def playerMove(self, l, c):
        self.__board.play(l, c, 'x')

    def computerMove(self):
        empty = self.__board.getFreeSquares()
        if len(empty) != 0:
            p = randint(0, len(empty) - 1)
            self.__board.play(empty[p].getx(), empty[p].gety(), 'y')
        return Square(empty[p].getx(), empty[p].gety())

    def isFull(self):
        return self.__board.isFull()

    def isWon(self):
        if self.__board.isFull() == True:
            return True
        return False

    def __str__(self):
        return str(self.__board)

    def getBoard(self):
        return self.__board

