def main() -> None:
    print(fib(7))  # 8
    print(fib(2))  # 1


def fib(n) -> int:
    """
      You must write the fib() function which takes in a positive integer,
      n, and returns the n-th Fibonacci number. However, instead of using
      recursion, your function must use any of the loops.
    """
    fib_list = []

    for i in range(n):
        if i == 0 or i == 1:
            fib_list.append(i)
        else:
            fib_list.append((fib_list[i-1]) + (fib_list[i-2]))

    return fib_list[n-1]


if __name__ == "__main__":
    main()
