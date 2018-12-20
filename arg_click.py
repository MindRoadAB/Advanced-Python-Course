########## Argparse & Click  Exercises ##########

############ Argparse  ##########

# Lab: argparse
'''import argparse

# First step: Instantiate the parser
parser = argparse.ArgumentParser(description="Simple program to find a square value for a given number from the user")

# Second Step:  Adding Arguments
parser.add_argument("square", type=float, default=1, help="Display a square of a given number")

# Third Step: ArgumentParser parses arguments through the parse_args() method, Which will check the command line
# and then will convert each argument to the type, then carry out the action
args = parser.parse_args()

# Access:
print(args.square ** 2)

# Check Values
if args.square == 0:
    parser.error("There's no square value for 0 number")'''


# Exercise 7
# Write a Python Program using the argparse method to build a calculator with the operations (add, sub, mult & div). Create two functions:
# •	def main (): Includes all the previous steps!
# •	def calc(args): Includes all the Calculators Operations.
# Run the program after building it as following:
#   	python arg_click.py -x 5 -y 6 -operation mult

'''import argparse
import sys


def main():
    # Creating a parser (an ArgumentParser object)
    parser = argparse.ArgumentParser(description='Script to do some operations for numbers')
    #  Adding Arguments
    # The first parameter is the name of the argument, the second parameter is the type of the variable,
    # The third parameter is a default value and finally help to display the parser help message.
    parser.add_argument('-x', type=float, default=1.0,
                        help='what is the first number?')

    parser.add_argument('-y', type=float, default=1.0,
                        help='what is the second number?')

    parser.add_argument('-operation', type=str, default='add',
                        help='what operation? (add, sub, mult, div)')

    # To save numbers in a Text file
    parser.add_argument("-o", "--output", help="Print the result to a file", action="store_true")


    args = parser.parse_args()
    if args.output:
        f = open("Calc.txt", "a")
        f.write(str(calc(args) + '\n'))
    else:
        sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return str(args.x + args.y)
    elif args.operation == 'sub':
        return str(args.x - args.y)
    elif args.operation == 'mult':
        return str(args.x * args.y)
    elif args.operation == 'div':
        return str(args.x / args.y)


if __name__ == '__main__':
    main()'''

# >python arg_click.py -h
# -h: is a short description of the argument, once the user asks for help,
# help description will be displayed with each argument

# >python arg_click.py -x 5 -y 6 -operation mult -o
# To print the result in a file.




