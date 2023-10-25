#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by: Joseph Du
#----------------------------------------------------


class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        try:       
            return self.items.pop()
        except IndexError:
            raise Exception('Stack is empty')
    
    def peek(self): 
        try:     
            return self.items[len(self.items)-1] 
        except IndexError:
            raise Exception('Stack is empty')
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
            self.items = []