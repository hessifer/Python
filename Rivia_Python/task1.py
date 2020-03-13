"""
Write a program to prompt the user for their first name and 
last name then display the full name with each odd element 
capitalized and each even element lowercase.
"""

def main():
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')

    while True:
        if not validate_name(first_name):
            first_name = input('Please enter your first name: ')
        elif not validate_name(last_name):
            last_name = input('Please enter your last name: ')
        else:
            break
    
    full_name = first_name + " " + last_name
    for i, c in enumerate(full_name):
        if i % 2 == 0:
            print(f"{c.lower()}", end='')
        else:
            print(f"{c.upper()}", end='')
    print()


def validate_name(name):
    return name.isalpha()

if __name__ == '__main__':
    main()