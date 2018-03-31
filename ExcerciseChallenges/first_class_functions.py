"""
Values in a language that are handled uniformly throughout are called "first class". They may be stored
in data structures, passed as arguments, or used in control structures. Languages which support values
with function types, and treat them the same as non-function values, can be said to have 
"first class functions".
"""

# Step 1: Create a function named "add" that adds two items after
# converting them to floats

# Step 2: Create a function named "multiply" that multiplies two items
# after converting them to floats

# Step 3. Use print, input, and your functions ONLY (No Variable Assignments) to collect enough numbers
# to run multiply(add(), add()) and output the product (You need 4 numbers)

# Extra Credit. Only convert to a float if the value entered is a float, if its a number convert to int,
# otherwise leave it alone. Account for exceptions! Then refactor your code in Step 3.

# Extra Credit
def convert(value):
    if '.' in value:
        try:
            return float(value)
        except ValueError as ve:
            pass
    if value.isnumeric():
        try:
            return int(value)
        except ValueError as ve:
            pass
    return value

# Step 1 Code Here
def add(num1, num2):
    return num1 + num2
    
# Step 2 Code Here
def multiply(num1, num2):
    return num1 * num2
    
# Step 3 Code Here
print(
    multiply(
        add(
            convert(input("Number 1: ")),
            convert(input("Number 2: "))
        ),
        add(
            convert(input("Number 1: ")),
            convert(input("Number 2: "))
        )
    )
)
        
