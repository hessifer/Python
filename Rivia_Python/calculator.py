# main entry of program
def main():
    # clean up whitespace
    user_input = input("Please enter only one of the following operators: (+, -, /, *):  ").strip()
    
    # validate input
    type_of_calculation =  validate_operator(user_input)  
    
    while True:
        try:
            number1 = int(input("Please enter your first number: " ))
            number2 = int(input("Please enter your second number: " ))
            break
        except ValueError:
            print("Your entry is not a valid number.")

    # Print the results
    results = calculate(type_of_calculation, number1, number2)
    if results:
        print(f"The result of this operation is: {results}")

def validate_operator(input_operator):
    # takes a string as an argument and validates
    # operation against (+, -, *, /)
    operators = {"+", "-", "*", "/"}

    while True:
        # check for membership
        if input_operator in operators:
            return input_operator
        else:
            input_operator = input("Please enter only one of the following operators: (+, -, /, *):  ")

def calculate(input_operator, input_number1, input_number2):
    if input_operator == '+':
        return get_addition(input_number1, input_number2)
    elif input_operator == '-':
        return get_substraction(input_number1,input_number2)
    elif input_operator == '*':
        return get_multiplication(input_number1,input_number2)
    else: 
        return get_division(input_number1,input_number2)

def get_multiplication(numberA, numberB):
    return numberA * numberB

def get_addition(numberA, numberB):
    return numberA + numberB

def get_division(numberA, numberB):
    try:
        return numberA // numberB
    except ZeroDivisionError:
        print("Dude, you can't divide by zero.")

def get_substraction(numberA, numberB):
    return numberA - numberB


if __name__ == "__main__":
     main()