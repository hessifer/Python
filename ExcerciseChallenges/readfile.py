import os


# Ask user to enter a file name, including full path
def get_file_name():
    """Asks the user for a file name and checks to make sure it exist before
    returning the filename.

    Returns: str -> filename
    """
    file_name = input('Please enter a file name, be sure to included the absolute path to the file: ')

    while not os.path.isfile(file_name):
        file_name = input('Please enter a file name, be sure to included the absolute path to the file: ')
    return file_name


# Ask the user what lines that want to display
def get_lines_of_txt(fh, start=1, stop=1):
    lines_of_txt_list = []

    for counter, line in enumerate(fh, 1):
        if counter in range(start, stop + 1):
            lines_of_txt_list.append(line)
    return lines_of_txt_list


# Display each line of text with the line number at the beginning, format it nicely
# TODO: Make sure they don't ask for more lines than the file contains
# TODO: If they don't want to add a stop line, use the last line in file
def main():
    while True:
        file = get_file_name()
        choice = input('Do you want to display specific lines within the file? [y/N]: ')

        if choice and choice.lower()[0] == 'y':
            start = int(input('What line number do you want to start at: '))
            stop = int(input('What line number do you want to stop at: '))
            with open(file, 'r') as fh:
                lines = get_lines_of_txt(fh, start, stop)

            for line in lines:
                print("{:>5}: {}".format(start, line))
                start += 1
        else:
            with open(file, 'r') as fh:
                for line_number, value in enumerate(fh, 1):
                    print("{:>5}: {}".format(line_number+1, value))
        # Ask the user if they want to view another file [Y/n]
        keep_going = input("Would you like to view another file [N/y]: ")
        if not keep_going or keep_going.lower()[0] == 'n':
            break


if __name__ == '__main__':
    main()
