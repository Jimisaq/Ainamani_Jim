from pycparser.ply.yacc import resultlimit

try:
    result=5/0
except ZeroDivisionError as e:
    print(e)
    print("Error: Division by zero is not allowed")
else:
    print("Result is: ", result)
finally:
    print("This block always executes, regardless of an exception")

#Exercise: Raise a custom exception that checks for positive numbers
class CustomException(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise CustomException("Number is not positive")
    else:
        print("Number is positive")

try:
    check_positive(-5)
except CustomException as e:
    print(e)
    print("Custom exception caught")

#Assignment 2:
#Write a program to handle errors, the program should ask for two numbers using input and then
#divides them. Use an infinite loop to keep asking until a valid input is provided.