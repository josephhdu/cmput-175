# Library program (Assignment 1)

def books():
    """Reads the books text file and returns a dicitnary containing all the information"""

    file = open('books.txt','r')
    books = file.readlines()
    file.close()
    booksDict = {}
    for i in books:
        info = i.split('#')
        bookNum = info.pop(0)
        info[-1] = info[-1].strip('\n')
        booksDict[bookNum] = info
    return booksDict

def students():
    """Reads the students text file and returns a dicitnary containing all the information"""

    file = open('students.txt','r')
    students = file.readlines()
    file.close()
    studentsDict = {}
    for i in students:
        info = i.split(',')
        studentNum = info.pop(0)
        info[-1] = info[-1].strip('\n')
        studentsDict[studentNum] = info
    return studentsDict

def borrowers():
    """Reads the borrowers text file and returns a dicitnary containing all the information"""

    file = open('borrowers.txt','r')
    borrowers = file.readlines()
    file.close()
    borrowersDict = {}
    for i in borrowers:
        info = i.split(';')
        borrowerNum = info.pop(0)
        info[-1] = info[-1].strip('\n')
        borrowersDict[borrowerNum] = info
    return borrowersDict
file = open('standing.txt', 'w')

def returns():
    """Reads the returns text file and returns a dicitnary containing all the information"""

    file = open('returns.txt','r')
    returns = file.readlines()
    file.close()
    returnsDict = {}
    for i in returns:
        info = i.split(';')
        returnsNum = info.pop(0)
        info[-1] = info[-1].strip('\n')
        returnsDict[returnsNum] = info
    return returnsDict

class Student():
    """Class used to store information(I didn't end up having enough time to use it)"""
    def __init__(self, student_name, student_class, book, due_date):
        self.student_name = student_name
        self.student_class = student_class
        self.book = book
        self.due_date = due_date

class Money():
    """Class used to store information(I didn't end up having enough time to use it)"""
    def __init__(self, student_name, money_owed, student_class):
        self.student_name = student_name
        self.money_owed = money_owed
        self.student_class = student_class

class Standing():
    """This class does all the processing of the inputted data and outputs into table format"""
    
    def __init__(self):
        """Initializes all the dictionaries from the other functions"""
        self.books = books()
        self.students = students()
        self.borrowers = borrowers()
        self.returns = returns()

    def table1(self):
        """Does the slicing into the dictionaries of the first table and prints out the first table
        
        bigBorrowerList - list that contains all the sliced info
        totalBooks - an integer that adds up total amount of books
        """
        bigBorrowerList = []
        totalBooks = 0

        # Main for loop that loops through the keys of the books
        for key in self.borrowers:
            borrowerList = []
            try:
                book_state = int(self.returns[key][2])
            except:
                pass

            # If the book isnt returned
            if book_state != 0:
                student_id = self.borrowers[key][0]
                student_name = self.students[student_id][0]
                student_grade = self.students[student_id][1]
                book = self.books[key][0]
                book_due_date = self.borrowers[key][2]

                date = {}
                date['month'] = book_due_date[2:4]
                date['day'] = book_due_date[4:6]
                date['year'] = book_due_date[0:2]
                
                #to change the month
                if date['month'] == '01':
                    date['month'] = 'Jan'
                elif date['month'] == '02':
                    date['month'] = 'Feb'
                elif date['month'] == '03':
                    date['month'] = 'Mar'
                elif date['month'] == '04':
                    date['month'] = 'Apr'
                elif date['month'] == '05':
                    date['month'] = 'May'
                elif date['month'] == '06':
                    date['month'] = 'Jun'
                elif date['month'] == '07':
                    date['month'] = 'Jul'
                elif date['month'] == '08':
                    date['month'] = 'Aug'
                elif date['month'] == '09':
                    date['month'] = 'Sep'
                elif date['month'] == '10':
                    date['month'] = 'Oct'
                elif date['month'] == '11':
                    date['month'] = 'Nov'
                elif date['month'] == '12':
                    date['month'] = 'Dec'

                # to change the year
                if date['year'] == '18':
                    date['year'] = '2018'
                elif date['year'] == '19':
                    date['year'] = '2019'
                elif date['year'] == '20':
                    date['year'] = '2020'
                elif date['year'] == '21':
                    date['year'] = '2021'
                elif date['year'] == '22':
                    date['year'] = '2022'
                elif date['year'] == '23':
                    date['year'] = '2023'
                dueDate = date['month'] + ' ' + date['day'] + ', ' + date['year']

                totalBooks = totalBooks + 1

                # Sends info the another class
                late_student = Student(student_name, student_grade, book, dueDate)

                # Appends all sliced info to the large list
                borrowerList.append(late_student.student_name)
                borrowerList.append(late_student.book)
                borrowerList.append(late_student.due_date)
                bigBorrowerList.append(borrowerList)

        # Write the information into new text file
        format1 = '+' + '-' * 18 + '+' + '-' * 37 + '+' + '-' * 14 + '+\n'
        heading1 = (f'| {"Student Name": <16.16} | {"Book": <35.35} | {"Due Date": <12.12} |\n')
        file.write(format1)
        file.write(heading1)
        file.write(format1)
        for i in bigBorrowerList:
            studentName = i[0]
            studentBook = i[1]
            dateReturn = i[2]
            file.write(f'| {studentName: <16.16} | {studentBook: <35.35} | {dateReturn: <12.12} |\n')
        file.write(format1)
        file.write(f'| {"Total Books": <54} | {totalBooks: >12} |\n')
        file.write(format1)

    def table2(self):
        """Does the slicing into the dictionaries of the first table and prints out the second table
        
        bigMoneyList - list that contains all the sliced info
        totalPrice - adds up all the prices of the books
        """
        bigMoneyList = []
        totalPrice = 0

        try:
        # Slices the data
            for key in self.returns:
                money = []

                bookState = int(self.returns[key][2])

                logical = bookState != 0 and bookState != 2 and bookState != 3

                if logical:
                    bookPrice = float(self.books[key][2])
                    studentId = self.returns[key][0]
                    studentName = self.students[studentId][0]
                    studentClass = self.students[studentId][1]

                    totalPrice = totalPrice + bookPrice
                    
                    money.append(studentName)
                    money.append(bookPrice)

                Money(studentName, bookPrice, studentClass)
                
                bigMoneyList.append(money)
            
            totalPrice = '$' + str(totalPrice)

            # Write the information into new text file 
            format2 = '+' + '-' * 18 + '+' + '-' * 10 + '+\n'
            heading2 = (f'| {"Student Name": <16.16} | {"Due": <8.8} |\n')
            file.write(format2)
            file.write(heading2)
            file.write(format2)
            for i in bigMoneyList:
                sname = i[0]
                bmoney = str(i[1])
                bmoney = '$' + bmoney
                file.write(f'| {sname: <16.16} | {bmoney: >8.8} |\n')
            file.write(format2)
            file.write(f'| {"Total Books": <16.16} | {totalPrice: >8.8} |\n')
            file.write(format2)
        except:
            file.write(format2)
            file.write(f'| {"Total Books": <16.16} | {totalPrice: >8.8} |\n')
            file.write(format2)

def main():
    """Main function that runs everything"""
    s1 = Standing()
    s1.table1()
    s1.table2()

main()