def get_smallest_positive_integer(numbers: list) -> int:
    """
    function that returns the smallest positive from a list of numbers
    :param numbers: integers list
    :return: smallest positive an integer from numbers
    """
    smallest_positive: int = 0

    if len(numbers) == 0:
        raise ValueError("Empty list")

    for number in numbers:
        if type(number) is not int:
            continue
        if number > 0:
            if number < smallest_positive or smallest_positive == 0:
                smallest_positive = number
    if smallest_positive == 0:
        raise ValueError("No positive integers found")
    return smallest_positive


def main():
    my_numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_nums: list = [5, 6, 7, 8, 9, 10]
    numbers: list = [4, -6, 7, 2, -4, 10]
    nums: list = []
    more_numbers = ["dog", "blue"]

    print(get_smallest_positive_integer(my_numbers))
    print(get_smallest_positive_integer(my_nums))
    print(get_smallest_positive_integer(numbers))
    print(get_smallest_positive_integer(more_numbers))
    print(get_smallest_positive_integer(nums))


if __name__ == "__main__":
    main()
