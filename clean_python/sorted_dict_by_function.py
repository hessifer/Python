#!/usr/bin/env python3

"""
   Purpose: Illustrate clean way to sort a
            dictionary using a function.
"""

def get_user_name(users):
    """Takes a dictionary and returns the key in lower case."""
    return users["first_name"].lower()


def get_sorted_dictionary(users):
    """Takes a dictionary object and sorts using function."""
    if not isinstance(users, list):
        raise ValueError("Not a correctly formatted list.")
    if not len(users):
        raise ValueError("Empty list.")
        
    users_by_name = sorted(users, key=get_user_name, reverse=False)
    return users_by_name


def main():
    users = [{"first_name": "Zeek", "age": 45},
             {"first_name": "Helen", "age": 39},
             {"first_name": "Buck", "age": 10},
             {"first_name": "Andrey", "age": 36}
             # {"name": "anni", "age": 9}
            ]
    # import pdb; pdb.set_trace()

    sorted_user_names = get_sorted_dictionary(users)
    print("{}".format(sorted_user_names))

if __name__ == "__main__":
    main()
