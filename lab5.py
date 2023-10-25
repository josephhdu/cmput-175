#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Asks for the users input to determine what they want to do
    Inputs: N/A
    Returns: userInput - the users input
    '''

    validInputs = ['=','<','>','q']
    userInput = input('Enter = to enter a URL, < to go back, > to go forward, q to quit:')
    if userInput not in validInputs:
        raise Exception('Invalid entry.')

    return userInput


def goToNewSite(current, bck, fwd):
    '''
    This function is for if the user wants to go to a new site
    Inputs: current - the current is the site the user is currently at
    bck - a list that contains the sites the user has visted in order to go back
    fwd - a list that contains the sites the user has visted in oder to go forward
    Returns: current - the new site the user is at
    '''   
    bck.push(current)
    current = input('URL:')
    fwd.clear()
    return current
    
def goBack(current, bck, fwd):
    '''
    This function is for the user to go back a site
    Inputs: current - the current is the site the user is currently at
    bck - a list that contains the sites the user has visted in order to go back
    fwd - a list that contains the sites the user has visted in oder to go forward
    Returns: current - the new site the user is at
    '''    
    try:
        bck.peek() # raises a exception if the list isn't filled
        fwd.push(current)
        current = bck.pop()
    except:
            print('Cannot go back')
    
    return current
        

def goForward(current, bck, fwd):
    '''
    This function is for the user to go forward a site
    Inputs: current - the current is the site the user is currently at
    bck - a list that contains the sites the user has visted in order to go back
    fwd - a list that contains the sites the user has visted in oder to go forward
    Returns: current - the new site the user is at
    '''    
    try:
        fwd.peek() # raises an exception is something is wrong
        bck.push(current)
        current = fwd.pop()
    except:
        print('Cannot go forward')

    return current



def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    