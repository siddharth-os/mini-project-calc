import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    result = 1
    for i in range(2, x+1):
        result *= i
    return result

def natural_logarithm(x):
    if x <= 0:
        raise ValueError("Cannot compute natural logarithm of a non-positive number")
    return math.log(x)

def power(x, y):
    return math.pow(x, y)

def calculator():
    while True:
        print("Scientific Calculator Options")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power Function")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        try:
            if choice == '1':
                x = float(input("Enter a number: "))
                result = square_root(x)
                print("Square root of {} is {}".format(x, result))
            elif choice == '2':
                x = int(input("Enter a number: "))
                result = factorial(x)
                print("{}! is {}".format(x, result))
            elif choice == '3':
                x = float(input("Enter a number: "))
                result = natural_logarithm(x)
                print("Natural logarithm of {} is {}".format(x, result))
            elif choice == '4':
                x = float(input("Enter a number: "))
                y = float(input("Enter the power: "))
                result = power(x, y)
                print("{} raised to the power of {} is {}".format(x, y, result))
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError as ve:
            print(ve)

if __name__ == '__main__':
    calculator()
