def factorial(num):
    """This recursive function calls
   itself and calculates the factorial of a number"""
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


# finding factorial
num = int(input("Enter a Number: "))
if num < 0:
    print("No factorial for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", factorial(num))
