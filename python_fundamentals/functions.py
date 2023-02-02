# function with no parameter
def say_hello():
    print("Hello!")


# function with one parameter
def greeting(message):
    print(f"{message}")


# function with two parameters
def add_two_numbers(num1, num2):
    return num1 + num2


# function with two parameters where one is a default value
def display_text(text, caps=False, add_dunder=False):
    if caps:
        if add_dunder:
            print(f"__{text.upper()}__")
        else:
            print(f"{text.upper()}")
    else:
        if add_dunder:
            print(f"__{text}__")
        else:
            print(f"{text}")


def find_color(colors):
    if len(colors) > 0:
        for color in colors:
            if len(color) > 3:
                print(color)





if __name__ == "__main__":
    # say_hello()
    # msg = "Python is fun!"
    # greeting(msg)
    # answer = add_two_numbers(4, 9)
    # print(answer)
    # display_text("coding", caps=True)
    # find_color(['yellow', 'blue', 'red'])
    find_color([])



