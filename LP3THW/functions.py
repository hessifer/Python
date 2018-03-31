"""this is our little calculator to work with functions."""


def add(num1, num2):
    """add num1 with num2 and return the results."""
    return num1 + num2


def subtract(num1, num2):
    """subtract num1 with num2 and return the results."""
    return num1 - num2


def multiply(num1, num2):
    """multiply num1 with num2 and return the results."""
    return num1 * num2


def divide(num1, num2):
    """divide num1 with num2 and return the resluts."""
    return num1 / num2


if __name__ == "__main__":
    print("Let's power on our calculator.")
    print("\nInitializing power sequence...")
    print()
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    print("\nInitializing calculation sequence...")
    print()
    print(f"The sum of your two numbers is: {add(num1, num2)}")
    print(f"The difference of your two numbers is: {subtract(num1, num2)}")
    print(f"The quotient of your two numbers is: {divide(num1, num2)}")
    print(f"The product of your two numbers is: {multiply(num1, num2)}")
