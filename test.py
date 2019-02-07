import unittest
from domain import *
class BoardTest(unittest.TestCase):

    def setUp(self):
        inpt = 5
        self.__board = Board(inpt)
        self.__game = Game(inpt)

    def test(self):
       self.assertRaises(Exception, self.__board.play,-1,2,"x")
       self.assertRaises(Exception, self.__board.play,0,9,"x")
       self.assertRaises(Exception, self.__board.play,0,"y","x")
       self.assertRaises(Exception, self.__board.play,0,1,"z")
       self.__board.play(0,1,"x")
       b1 = str(self.__board)
       self.assertEqual(b1,"   0 1 2 3 4 " + "\n"
                           "0: 0 x 0 0 0 " + "\n"
                           "1: 0 0 0 0 0 " + "\n"
                           "2: 0 0 0 0 0 " + "\n"
                           "3: 0 0 0 0 0 " + "\n"
                           "4: 0 0 0 0 0 " + "\n")

       self.__board.play(1, 3, "y")
       b2 = "   0 1 2 3 4 " + "\n" +"0: 0 x 0 0 0 " + "\n"+ "1: 0 0 0 0 0 " + "\n" + "2: 0 0 0 0 0 " + "\n"+ "3: 0 0 0 0 0 " + "\n" + "4: 0 0 0 0 0 " + "\n"
       b3 = str(self.__board)
       self.assertNotEqual(b1,b3)
       self.__board.play(3, 3, "x")
       self.__game.computerMove()
       self.__board.play(2, 1, "x")

       self.assertEqual(self.__board.isFree(2,1), False)
       self.assertEqual(self.__board.isFree(4,1), True)
       self.__board.play(4, 1, "y")
       self.assertEqual(self.__game.isWon(), False)
if __name__ == "__main__":

    unittest.main()
