"""Example usage of argv."""


import sys


def main():
    if len(sys.argv) >= 2:
        for i, value in enumerate(sys.argv):
            print(f"Argument Index: {i}\t Argument Value: {value}")    
    else:
        sys.exit("ERROR: you did not specify any arguments.")


if __name__ == '__main__':
    main()
