"""
Task7: Create a program that ask the user for a file to read from. If that file
does not exist handle the proper exception, by displaying a message ERROR:
File does not exist.
If the file exist, display the contents.
"""


def main():
    file_to_read = input("Please enter the absolute path to the \
file you want me to read: ")

    try:
        with open(file_to_read) as fh:
            for line in fh:
                print(line)
    except FileNotFoundError:
        print(f"ERROR: {file_to_read} does not exist.")


if __name__ == '__main__':
    main()
