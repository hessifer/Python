"""
Write a function that parses the file /etc/passwd and returns a unique
set of users. Handle any errors that may occurr and then test your funciton
works as expected.
"""


def main():
    for i in get_unique_users('/etc/passwd'):
        print(f"{i}")


def get_unique_users(file):
    users = set()

    with open(file) as fh:
        for line in fh:
            users.add(line.split(':')[0])
    return users


if __name__ == '__main__':
    main()
