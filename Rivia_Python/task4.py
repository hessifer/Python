"""
Given space-separated integers as input, create
 a tuple (t) of those  integers. Then compute and print the result of
 hash(t).

Note: hash() is one of the functions in the __builtins__ module, 
so it need not be imported.
"""

def main():
    numbers = input('Please enter your numbers here: ').split()

    try:
        results = tuple(map(int, numbers))
    except ValueError as ve:
        print(f"{ve}")
    else:
        print(hash(results))


if __name__ == '__main__':
    main()