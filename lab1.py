# The items that Bluebell Greenhouses sell stored in dictionary
items = {'daffodil':0.35, 'tulip':0.33, 'crocus':0.25, 'hyacinth':0.75, 'bluebell':0.50}

# The Items Mary buys every year in dictionary
maryItems = {'daffodil':50, 'tulip':100}

# Tulip inflation
# Calculates the increase for Tulip price
tulipInflation = items['tulip'] = items['tulip'] * 1.25
tulipInflation = '% 5.2f' % tulipInflation
tulipInflation = float(tulipInflation)
items['tulip'] = tulipInflation

# Mary's hyaciths, adds the hyaciths to the order
maryItems['hyacinth'] = 30

# Mary's purchase
# Creates a list for Mary's stuff
maryStuff = []
for i in maryItems.keys():
    thing = i[0:3]
    thing = thing.upper()
    maryStuff.append(thing)

# Calculates Mary's totals for each item
total = {'daf':0, 'tul':0, 'hya':0}
total['daf'] = float(maryItems['daffodil']*items['daffodil'])
total['tul'] = float(maryItems['tulip']*items['tulip'])
total['hya'] = float(maryItems['hyacinth']*items['hyacinth'])

# Calculates the total prices and blubs
price = 0
bulbs = 0
for i in total.values():
    price = price + i
for i in maryItems.values():
    bulbs = bulbs + i

# Prints the output
print('You have purchased the following bulbs')
print('%-5s *%4d = $ %6.2f' % (maryStuff[0], maryItems['daffodil'], total['daf']))
print('%-5s *%4d = $ %6.2f' % (maryStuff[1], maryItems['tulip'], total['tul']))
print('%-5s *%4d = $ %6.2f' % (maryStuff[2], maryItems['hyacinth'], total['hya']))
print('Thank you for purchasing %d bulbs from Bluebell Greenhouses. \nYour total comes to %5.2f.' % (bulbs,price))



#Rainfall 
rainfall = []
sixty_seventy = []
seventy_eighty = []
eighty_ninety = []
ninety_plus = []

# Reads file
file = open('rainfall.txt', 'r')
file.close

# Appends content to a big list
for i in range(25):
    contents = file.readline()
    split_str = contents.split()
    rainfall.append(split_str)

# Sorts the big list into smaller lists based on rainfall
for i in rainfall:
    number = float(i[1])
    if 60 <= number <= 70:
        sixty_seventy.append(i)
    elif 70 <= number <= 80:
        seventy_eighty.append(i)
    elif 80 <= number <= 90:
        eighty_ninety.append(i)
    elif 90 <= number <= 100:
        ninety_plus.append(i)

# Converts rainfall to float values
for i in range(len(sixty_seventy)):
    sixty_seventy[i][1] = float(sixty_seventy[i][1])
for i in range(len(seventy_eighty)):
    seventy_eighty[i][1] = float(seventy_eighty[i][1])
for i in range(len(eighty_ninety)):
    eighty_ninety[i][1] = float(eighty_ninety[i][1])
for i in range(len(ninety_plus)):
    ninety_plus[i][1] = float(ninety_plus[i][1])

# Sorts the second index of the lists
sixty_seventy.sort(key = lambda x: x[1])
seventy_eighty.sort(key = lambda x: x[1])
eighty_ninety.sort(key = lambda x: x[1])
ninety_plus.sort(key = lambda x: x[1])

# Writes the output into a new file
newFile = open('rainfallfmt.txt','w')
newFile.write('[50-60 mm)\n[60-70 mm)\n')
for i in sixty_seventy:
    newFile.write('           ')
    newFile.write(i[0])
    newFile.write('           ')
    newFile.write(str(i[1]))
    newFile.write('\n')
newFile.write('[70-80 mm)\n')
for i in seventy_eighty:
    newFile.write('           ')
    newFile.write(i[0])
    newFile.write('           ')
    newFile.write(str(i[1]))
    newFile.write('\n')
newFile.write('[80-90 mm)\n')
for i in eighty_ninety:
    newFile.write('           ')
    newFile.write(i[0])
    newFile.write('           ')
    newFile.write(str(i[1]))
    newFile.write('\n')
newFile.write('[90-100 mm)\n')
for i in ninety_plus:
    newFile.write('           ')
    newFile.write(i[0])
    newFile.write('           ')
    newFile.write(str(i[1]))
    newFile.write('\n')

newFile.close