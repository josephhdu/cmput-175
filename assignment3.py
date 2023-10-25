#----------------------------------------------------
# Assignment 3, Task 4(this doesn't work fully because I couldn't finish task 3 but this is what task 4 would've looked like)
# 
# Author: Joseph Du
# Collaborators: Shinto Kai, Zenan Kaminskas
#----------------------------------------------------


from AbacoStack import aStack, bStack, Card

if __name__ == '__main__':
    stacks = input('How many stacks are there? ')
    depth = input('How deep is each stack? ')
    abaco = aStack(stacks, depth)

    continueGame = True
    while not continueGame:
        abaco.show()
        move = input("What is the your move?")
        if move == "Q":
            break
        elif move =="R":
            abaco.reset()
        abaco.moveBead(move)
        if abaco.isSolved(Card.basicStr()) == True:
            continueGame = False