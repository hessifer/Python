def main():
    """The main entry of program."""
    print(smallest_positive([4, -6, 7, 2, -4, 10]))
    print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
    print(smallest_positive([-6, -9, -7]))
    print(smallest_positive([]))


def smallest_positive(numbers):
    """Returns smallest positive number in numbers."""
    smallest = None

    if numbers:
        for num in numbers:
            if num > 0:
                if smallest:
                    if num < smallest:
                        smallest = num
                else:
                    smallest = num
    return smallest


if __name__ == "__main__":
    main()
