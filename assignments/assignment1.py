#factorial of a number
def factorial(num):
    if num <0:
        return 0
    elif num == 0 or num == 1:
        print("num is zero")
        return 1
    else:
        return factorial(num-1)*num

print(factorial(0))