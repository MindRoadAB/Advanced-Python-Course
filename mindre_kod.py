####### Use Less Code #########

# Exercise1
# Write a Python Program to generate a list and a tuple with given numbers from the user, the numbers are separated by using comma and print the result for both list and tuple types.
# Sort the given numbers in ascending and descending order and print the numbers in a comma separated sequence. Make sure to remove any duplicate numbers in the
# list before sorting.
# Hint: split(), sort(), join(), revers().

values = input("Input the sequence of numbers: ")

my_list = values.split(',')
tuple = tuple(my_list)
print(f"list: {my_list}")
print(f"Tuple: {tuple}")

new_list = list(set(my_list))

new_list.sort()
print("Sorted list: ", new_list)
new_list.sort(reverse=True)
print("Sorted reversed list: ", new_list)


# Exercise2
# Write a Python program that calculate the number of lower, upper care letters, space and digits.
# Create an input field that allows the user to enter a sentence and shows the number(s) of upper and lower case letter()s,
# as well as the number(s) of pressing space and the number(s) of digit(s).
# Hint: for, def, islower(), dict ={" upper": 0}


def check_str(char):
    no = {"Upper_case": 0, "Lower_case": 0, "Space": 0, "Digit": 0}
    for check in char:
        if check.islower():
            no["Lower_case"] += 1
        elif check.isupper():
            no["Upper_case"] += 1
        elif check.isdigit():
            no["Digit"] += 1
        else:
            no["Space"] += 1
    return no


string_sent = input("Enter any sentence: ")
no_char = check_str(string_sent)
print("The number(s) of Upper Case letters: ", no_char["Upper_case"])
print("The number(s) of Lower Case letters: ", no_char["Lower_case"])
print("The number(s) of Space: ", no_char["Space"])
print("The number(s) of Digit: ", no_char["Digit"])

# Write the same program as in the Ex3 but using regular expression method!
# Hint: import re, r"[A-Z]", re.findall

import re


def check_str(char):
    upper_case = r"[A-Z]"
    lower_case = r"[a-z]"
    space_case = r" "
    digit_case = r"[0-9]"

    # Using findall
    num_case = r"\d+"
    num = re.findall(num_case, char)

    if not num:
        print("You haven't type any digit numbers")
    else:
        print("The extracted numbers from the string ", num)

    # Using Sub, The /D character(non digit) can be replaced by an empty string!
    num = re.sub("\D", "", char)
    print(num)

    # Using Filter and Lambda
    num = list(filter(lambda x: x.isdigit(), char))
    if not num:
        print("You haven't type any digit numbers")
    else:
        print("The extracted numbers from the string ", num)

    check_upper = re.findall(upper_case, char)
    print("The number of Upper Case letters: " + str(len(check_upper)))
    check_lower = re.findall(lower_case, char)
    print("The number of Upper Case letters: " + str(len(check_lower)))
    check_space = re.findall(space_case, char)
    print("The number of Space: " + str(len(check_space)))
    check_digit = re.findall(digit_case, char)
    print("The number of Digit: " + str(len(check_digit)))


check_str(input(" Enter any sentence: "))

# Exercise 3
# Write a Python program to find the longest and shortest word in a file!
# Hint: Use import re, re.compile(), findall(), lambda(To find the longest or shortest word)


import re


def long_short_word(f):
    with open(f, "r") as file:
        words = file.read()

    pattern = "\w+"
    regex = re.compile(pattern)
    word_found = regex.findall(words)

    long_word = max(word_found, key=lambda x: len(x))
    #    print(long_word)
    return long_word

    short_word = min(word_found, key=lambda x: len(x))
    return short_word


#    print(short_word)

long_short_word("employee_Salary.txt")


def fib_gen():
    n, m = 0, 1
    while n < 50:
        yield n
        n, m = m, n + m


# Exercise 4
# Write a Python Program using iterator to return the Fibonacci numbers below 50!
# Write the same program using generator.

def fib_gen():
    n, m = 0, 1
    while n < 50:
        yield n
        n, m = m, n + m



for fib_num in fib_gen():
    print(f"{fib_num}")


class Fibonancci:
    def __init__(self, fibNum):
        self.fibNum = fibNum

    def __iter__(self):
        self.n = 0
        self.m = 1
        return self

    def __next__(self):
        fib = self.n
        if fib > self.fibNum:
            raise StopIteration
        self.n, self.m = self.m, self.n + self.m
        return fib


_fibonancci = Fibonancci(50)
itr = iter(_fibonancci)
while True:
    print(next(itr))


# Exercise 5
# Create a Python class (Employee) holding data attributes (first_name, last_name, salary).
# The Employee class has two methods; one to greet the employee his/her full name and the other to get the salary after
# taking the tax. Print out the Full name and Salary after the tax.
# Create a decorator that wraps these methods to print out the method name as a heading before printing the result of the method.


def decorator(original_func):
    def wrapper(*args, **kwargs):
        print("{0}".format(original_func.__name__))
        print("-" * len(original_func.__name__))
        return original_func(*args, **kwargs) + "\n"

    return wrapper


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @decorator
    def greeting(self):
        return "Hello " + self.first_name + " " + self.last_name + " & Welcome to MindRoad Academy "

    @decorator
    def Salary_tax(self):
        return " The Given salary is " + str(self.salary - self.salary * 0.23) + " Swedish krona after tax"


employee = Employee("Tony", "Homsi", 30000)
print(employee.greeting())
print(employee.Salary_tax())

# Exercise 6
# Create a Python Program that calculates the time consumption for the square range of numbers!
# Create the function time_calc and the decorator @time_calc to measure the time.
# Hint: import time, time.time()


import time


def time_calc(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{func.__name__} function is finished , {run_time* 1000} msec")
        return result

    return wrapper_timer


@time_calc
def square(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result


array = range(1, 100000)
_square = square(array)
