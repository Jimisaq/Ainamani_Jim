#Assignment 2:
#Write a program to handle errors, the program should ask for two numbers using input and then
#divides them. Use an infinite loop to keep asking until a valid input is provided.
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
    else:
        print(f"The result of dividing {num1} by {num2} is {result}")
        break