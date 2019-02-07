import sys
from domain import *
class UI():
    def __init__(self, inpt):
        self.__inpt = inpt
        self.__game = Game(inpt)

    def gameUI(self):
        print('\033 Start Game : ')
        player = True
        while self.__game.isFull() != True:
            if player:
                sys.stdout.write("\033[;1m")
                try:
                    cmd = input("Give position <line>,<column> \n:")
                    cmd = cmd.strip().split(',')
                    cmd = [int(x) for x in cmd]
                    if len(cmd) != 2:
                        raise Exception("Command format <line>,<column>")
                    self.__game.playerMove(cmd[0], cmd[1])
                    player = False
                    sys.stdout.write("\033[1;34m")
                    print("Player move :")
                    if self.__game.isWon() == True:
                        sys.stdout.write("\033[1;34m")
                        print("PLAYER won!")
                        print(str(self.__game))
                        break

                except Exception as e:
                    print(e)
            else:
                sys.stdout.write("\033[0;32m")
                print("Computer move :")
                s = self.__game.computerMove()
                if self.__game.isWon() == True:
                    sys.stdout.write("\033[1;31m")
                    print("PC won!")
                    print(str(self.__game))
                    break
                player = True

            print(str(self.__game))
