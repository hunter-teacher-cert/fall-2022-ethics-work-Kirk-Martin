##Kirk Martin
#NIM.PY file
#CSCI 77800 
#FALL 2022 Ethics
#

import math


class Nim :
    @staticmethod
    def main( args) :
        stones = 12
        stonesTaken = 0
        print   ("Python-inputs")
        # loops until the game ends
        while (stones > 0) :
            # user input
            print("please enter a number from  1 -3")
            stonesTaken = input()
            # subtract from the stones
            stones = stones - stonesTaken
            print("There are this amount of stones " + str(stones) + " left")
            # if conditional if stones is less than or equal to zero you win
            if (stones <= 0) :
                print("You win!")
            # computers turn
            print("Computers Turn")
            stonesTaken = int((random() * 3)) + 1
            # subtract from stones
            stones = stones - stonesTaken
            print("The computer took " + str(stonesTaken))
            print("There are " + str(stones) + " left")
            print("         ")
            print("         ")
            print("         ")
            # if conditional if stones is less than or equal to zero Computer wins
            if (stones <= 0) :
                print("Computer wins!")
    

if __name__=="__main__":
    Nim.main([])
