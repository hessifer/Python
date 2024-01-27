def prod(num1, num2):
    return num1 * num2


def factorial_generator():
    """
    number n, n factorial is denoted by n!, and it is the product of all positive integers less than or equal to n.
    :param num: number to calculate
    :return: factorial of num
    """
    i = 1
    n = i

    while True:
        result = prod(n, i)
        yield result
        i += 1
        n = result


def main():
    fact_gen = factorial_generator()
    num = 5
    for i in range(num):
        print(next(fact_gen))


if __name__ == "__main__":
    main()
