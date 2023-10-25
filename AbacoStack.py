#----------------------------------------------------
# Assignment 3, Task 1,2,3(note task 3 some meathods aren't finished I couldn't get them to work)
# 
# Author: Joseph Du
# Collaborators: Shinto Kai, Zenan Kaminskas
#----------------------------------------------------

# imported modules
import random

class Card:

    def __init__(self, colours, depth):
        """
        Initializes a list to store all the beads
        :colours: is the amount of colours that are in stacks
        :depth: is how deep each stack goes
        """
        self.colours = colours
        self.depth = depth
        self.length = colours
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        alphabet = alphabet[0: colours]

        # adds beads to the list depending on init inputs
        self.__beads = []
        for i in range(self.length):
            for j in range(self.depth):
                self.__beads.append(alphabet[i])
        random.shuffle(self.__beads)

    def reset(self):
        """
        Resets the list beads
        """
        random.shuffle(self.__beads)
        return self.__beads

    def show(self):
        """
        Formats the list of beads to display the card
        """
        print(self.__beads)
        for i in range(self.depth):
            print("|", end="")
            for j in range(self.length):
                if j > 0:
                    print("", end=" ")
                print(self.__beads[self.depth * j + i], end="")
            print("|")

    def basicStr(self):
        """
        Returns the list of beads as a string
        """
        bString = "".join(self.__beads)
        return bString

    def abacoShow(self):
        """
        Formats the list of beads in a list with lines to use to print card in abaco stack
        """
        show = []
        for i in range(self.depth):
            string = ''
            string += '|'
            for j in range(self.colours):
                if j > 0:
                    string += ' '
                string += self.__beads[self.depth * j + i]
            string += '|'
            show.append(string)
        return show

    def stack(self, number):
        """
        returns the stack based on the number out of the stacks in the list
        :number: is an input int value that chooses which stack to return
        """
        if number > self.length:
            raise Exception("Stack does not exist")
        start = number * self.depth - self.depth #slicing to get the right stack
        end = start + self.depth
        return self.__beads[start:end]

    def __str__(self):
        """
        A string meathod that returns all the beads as a string
        """
        i = self.depth
        info = self.__beads.copy()
        while i < len(info):
            info.insert(i,"||")
            i += self.depth + 1
        info.insert(0, "|")
        info.append("|")
        aString = "".join(info)
        return aString
            
    def replace(self, filename,n):
        """
        Reads a the nth line out of a inputed file and retruns contents
        :filename: a name of a file
        :n: an int that gives which line to take out of the file
        """
        file = open(filename,"r")
        data = file.readlines()
        return data[n-1]

class bStack:

    def __init__(self, capacity):
        """
        initializes a list as to store the stack
        :capacity: an inputed value to create the bound for the bounded stack
        """
        self.stack = []
        self.capacity = capacity

    def push(self,item):
        """
        Adds the item into the first position of the list
        :item: the element that is going to be pushed onto the list
        """
        if len(self.stack) > self.capacity:
            raise Exception("Stack is full")

        self.stack.insert(0,item)

    def pop(self):
        """
        Removes the first element in the list
        """
        return self.stack.pop(0)

    def peek(self):
        """
        Returns the first element in the list
        """
        return self.stack[0]

    def show(self):
        """
        Shows the stack
        """
        print(self.stack)

    def getter(self):
        """
        Returns the stack
        """
        return self.stack

    def empty(self):
        """
        Empties the stack
        """
        return self.stack == []

    def size(self):
        """
        returns the size of the stack
        """
        return len(self.stack)

    def isFull(self):
        """
        returns if the Stack is full or not
        """
        return len(self.stack) == self.capacity

    def __str__(self):
        """
        Converts the stack into a string
        """
        return " ".join(self.stack)

class aStack:

    def __init__(self, stacks, depth):
        """
        Intialies the main list of stacks and other lists that need to be used
        :stacks: An inputed amount of stacks
        :depth: An inputed depth for the stacks
        """
        self.moves = 0
        self.stackNum = int(stacks)
        self.depth = int(depth)

        # Creates the list that goes on top of stack
        self.topList = []
        for i in range(self.stackNum + 2):
            self.topList.append(".")
        
        # List the represents the coloums
        self.numList = []
        for i in range(self.stackNum + 2):
            self.numList.append(i)

        #Creates a the list of stacks
        self.stackList = []
        for i in range(self.stackNum):
            stack = bStack(self.depth)
            self.stackList.append(stack)
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        for i in range(self.stackNum):
            for j in range(self.depth):
                self.stackList[i].push(alphabet[i])
        # for i in self.stackList:
        #     print(i)

        # for show meathod(doesn't work)
        self.card = Card(self.stackNum,self.depth)
        self.abacoshow = self.card.abacoShow()

    def moveBead(self, move):
        """
        Takes a move input and checks conditions to see if its is valid if yes it moves the bead
        :move: A two character input representing an index and a direction
        """
        moves = ["u", "d", "l", "r"]
        index = int(move[0])
        direction = move[1]
        
        #Check if it is a valid input
        if len(move) != 2:
            raise Exception("Error:invalid move")
        else:
            if direction not in moves:
                raise Exception("Error:invalid move")
            else:
                if index < 0 or index > len(self.topList) - 1:
                    raise Exception("Error:invalid move")


        try:
        # code to move item up(isn't finished, doesn't fully work)
            if direction == "u":
                if index == 0 or index == len(self.topList) - 1:
                    raise Exception("Error:invalid move")
                else:
                    if self.topList[index] != ".":
                        raise Exception("Error:invalid move")
                    else:
                        if self.stackList[index - 1].peek() != ".":
                            item = self.stackList[index - 1].pop()
                            self.topList[index] = item
                            self.stackList[index - 1].push(".")
                        else:
                            deep = 0
                            pass
                            # You would write a loop to go as deep as the stack is to find the non . element then pop up
                            
        # code to move item down(isn't finished)
            if direction == "d":
                if index == 0 or index == len(self.topList) - 1:
                    raise Exception("Error:invalid move")
                else:
                    if self.topList[index] != ".":
                        raise Exception("Error:invalid move")
                    else:
                        pass
                         # You would write a loop to go as deep as the stack is to find the non . element then pop up
        
        # code to move item right
            if direction == "r":
                if index == len(self.topList) - 1:
                    raise Exception("Error:invalid move")
                else:
                    if self.topList[index] == ".":
                        raise Exception("Error:invalid move")
                    else:
                        if self.topList[index + 1] != ".":
                            raise Exception("Error:invalid move")
                        else:
                            self.topList[index + 1] = self.topList[index]
                            self.topList[index] = "."
        
        # code to move item left
            if direction == "l":
                if index == 0:
                    raise Exception("Error:invalid move")
                else:
                    if self.topList[index] == ".":
                        raise Exception("Error:invalid move")
                    else:
                        if self.topList[index - 1] != ".":
                            raise Exception("Error:invalid move")
                        else:
                            self.topList[index - 1] = self.topList[index]
                            self.topList[index] = "."

        except:
            raise Exception("Error:invalid move")

    def isSolved(self, card):
        """
        Checks if the state of your stacks is the same as the card
        :card: the card to check if its solved
        """
        totalList = []
        for stack in self.stackList:
            info = stack.getter()
            for i in info:
                totalList.append(i)
        state = "".join(totalList)
        if state == card:
            return True
        else:
            return False

    def reset(self):
        """
        Resets the card and refills the stack list
        """
        self.moves == 0 
        self.stackList = []
        for i in range(self.stackNum):
            stack = bStack(self.depth)
            self.stackList.append(stack)

        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

        for i in range(self.stackNum):
            for j in range(self.depth):
                self.stackList[i].push(alphabet[i])

        return self.stackList

    def show(self):
        """
        Shows the state of the stacks and displayes the card
        (I couldn't get this function to work right)
        """
        # a meathod I wrote in card to try and get it do work
        showCard = Card.abacoShow()

        # print the start of the display
        for number in range(len(self.numList)):
            print(self.numList[number], end=' ')
        print('')
        for bead in range(len(self.topList)):
            print(self.topList[bead], end=' ')
        
        
        #Below is code I wrote that didn't end up working
        # print('      card')
        # index = 0
        # for i in range(1, self.depth + 1):
        #     print('|', end=' ')
        #     for stack in self.stackList:
        #         stack = str(stack)
        #         print(stack[i], end=' ')
        #     print('|', end='')
        #     print(f'     {self.abacoshow[index]}')
        #     index += 1
        # print('+' + '-' + '-' * self.stackNum * 2 + '+'+  '            ', self.moves, 'moves')

        # Other stuff i tried that didn't end up working
        # for i in range(self.depth):
        #     print("|", end="")
        #     for j in range(self.numList):
        #         if j > 0:
        #             print(" ", end=" ")
        #         print(self.stackList[self.depth * j + i], end="")
        #     print("|")

       

if __name__ == '__main__':
    # Testing
    
    c = Card(3,3)
    c.show()
    print(c.stack(2))
    print(c.__str__())
    print(c.replace("replace.txt", 3))
    print(c.basicStr())

    
    
    s = bStack(2)
    s.push('a')
    s.push('b')
    s.show()
    print(s.__str__())
    s.push('c')
    
    
    abaco = aStack(3,3)
    print(abaco.isSolved("AAABBBCCC"))
    print(abaco.reset())
    abaco.moveBead("1u")
    abaco.show()