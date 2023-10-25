#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: Joseph Du
# Collaborators/references:
#----------------------------------------------------
def getAction():
    '''
    Asks for the users input to determine what they want to do
    Inputs: N/A
    Returns: userInput - the users input
    '''
    validInput = False
    validInputs = ['=','<','>','q']
    while not validInput:
        userInput = input('Enter = to enter a URL, < to go back, > to go forward, q to quit:')
        if userInput in validInputs:
            validInput = True
            return userInput
        else:
            print('Invalid entry.')


def goToNewSite(current, pages):
    '''
    This function is for if the user wants to go to a new site, also manages if the user goes back and then goes to new site
    Inputs: current - the current index of the list of sites that the user is at
    pages - a list that contains the sites that the user is visiting
    Returns: current - the update index after the action
    '''   
    website = input('URL: ')
    while len(pages) != current + 1:
        for i in pages:
            if pages.index(i) > current:
                pages.remove(i)
    current = current + 1
    pages.append(website)

    return current

    
def goBack(current, pages):
    '''
    This function is for the user to go back a site
    Inputs: current - the current index of the list of sites that the user is at
    pages - a list that contains the sites that the user is visiting
    Returns: current - the update index after the action
    '''    
    if current == 0:
        print('Cannot go back.')
    else:
        current = current - 1
    
    return current


def goForward(current, pages):
    '''
    This function is for the user to go forward a site
    Inputs: current - the current index of the list of sites that the user is at
    pages - a list that contains the sites that the user is visiting
    Returns: current - the update index after the action
    '''    
    if current >= len(pages) - 1:
        print('Cannot go forward')
    else:
        current = current + 1
        
    return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites,)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites,)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    
        
if __name__ == "__main__":
    main()