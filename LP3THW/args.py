"""a simple program to play with args from the command line"""

import sys


def show_command_line_args():
    """working with command line args to display length and values"""

    arg_length = len(sys.argv)
    print(f"Number of Command Line Arguments: {arg_length}")
    print(f"Comannd Line Argument Values: {' '.join(sys.argv)}")


def a_function_with_undetermined_args(*args):
    """show me what was passed into this function."""

    for arg in args:
        print(f"{arg}", end=" ")
    print()


if __name__ == "__main__":
    # how can we check if we have any command line arguments before
    # attempting to call/invoke/run the function below?
    show_command_line_args()

    # let's pass in our gracery list to a function
    print("The arguments passed to our function are: ", end="")
    a_function_with_undetermined_args("eggs", "bread", "milk", "oranges")
