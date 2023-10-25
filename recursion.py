# Exercise 1
some_list = [43,76,97,86]

def mylen(some_list):
    assert isinstance(some_list, list), "Must be a list" 
    if some_list == []:
        return 0 
    else:
        return 1 + mylen(some_list[1:])

print(mylen(some_list))

# Exercise  2

def intDivision(dividend, divisor):
    if dividend < divisor:
        answer = 0  
    else:
        answer = 1 + intDivision(dividend - divisor, divisor)

    return answer


n = int(input('Enter a integer dividend: '))
m = int(input('Enter a integer divisor: '))
print(intDivision(n,m))

# Exercise 3

def sumdigits(number):
    number = str(number)
    if len(number) == 0:
        sum = 0 
    else:
        sum = int(number[0]) + sumdigits(number[1:])
    return sum

number = int(input('Enter a number'))
print(sumdigits(number))

# Exercise 4

def reversedisplay(number):
    assert number > 0, "number must be postive"
    number = str(number)
    if number == "":
        return number
    else:
        return number[-1] + reversedisplay(number[:-1])

number = int(input("Enter a number"))
print(int(reversedisplay(number)))

# Exercise 5


def binary_search2(some_list, low, high, target):
    if high >= low:
        guess = (high + low) // 2
 
        if some_list[guess] == target:
            return guess

        # left side
        elif some_list[guess] > target:
            return binary_search2(some_list, low, guess - 1, target)
 
        # right side
        else:
            return binary_search2(some_list, guess + 1, high, target)
 
    else:
        return "Item is not in list"


someList = [-8,-2,1,3,5,7,9]

print(binary_search2(someList, 0, len(some_list) - 1, 3))
print(binary_search2(someList, 0, len(some_list) - 1, -8))