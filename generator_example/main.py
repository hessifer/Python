def all_evens():
    n = 0
    while True:
        yield n
        n += 2


def sum_nums(n: int, m: int) -> int:
    return n + m


def main():
    my_gen = all_evens()

    for i in range(5):
        print(next(my_gen))

    num1: int = 69
    num2: int = 1

    print()
    print(f"The sum of {num1} and {num2} is {sum_nums(num1, num2)}")
    print()
    for i in range(100):
        print(next(my_gen))


if __name__ == "__main__":
    main()
