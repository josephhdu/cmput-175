# This code takes the key and message from an inputed text file and decrypts it

def getInputFile():
    """ This fuction asks for the users input until the user inputs a correct input"""
    correct = False
    file = ''
    textFile = input('Enter the input filename:')
    # While statement to check if the input is valid
    while correct == False:
        if textFile == 'secretMessage1.txt':
            correct == True
            file = 'secretMessage1.txt'
            return file
        elif textFile == 'secretMessage2.txt':
            correct == True
            file = 'secretMessage2.txt'
            return file
        else:
            correct == False
            textFile = input('Invalid filename extension. Please re-enter the input filename:')

def decript(filename):
    """ This function takes decripts the message and print it"""
    # Reads the file and initializes some varibles
    file = open(filename,'r')
    key = file.readline()
    message = file.readline()
    key = int(key)
    message = message.lower()
    # tried to use strip()
    message = message.replace(' ','b')
    unicodelist = []

    # Changes the message into unitext number
    for i in message:
        new = ord(i)
        unicodelist.append(new)

    # Decripts ceaser cypher
    for i in range(len(unicodelist)):
        temp = unicodelist[i]
        for j in range(key): 
            temp = temp - 1 
            if temp < 97:
                temp = 122            
        unicodelist[i] = temp
    
    # Turns the numbers into characters and joins them into a string
    decriptMessage = []
    for i in unicodelist:
        char = chr(i)
        decriptMessage.append(char)
    string = ''.join(decriptMessage)
    string = string.replace('v',' ')
    print('The decripted message is:')
    print(string)

file = getInputFile()
decript(file)