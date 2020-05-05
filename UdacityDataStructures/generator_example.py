"""
A generator in Python is similar to a function except instead of returning a value and exiting a process,
a generator will pause the process, saving its state for next time. The biggest difference between a function
and generator from a code perspective is one word: return is changed to yield.

A generator becomes very useful when dealing with very large collections of data that you don’t want to
store in memory all at once. It’s also very useful for dealing with extremely large or even infinite series.

Below is an example of how to use a generator to print even numbers. Printing all even numbers at once
would take an infinite amount of time, but the generator allows the process to pause, and go back to
creating even numbers when needed.

To create the next successive even number simply call next() on the generator object, and it will
yield the next iteration. After yield is called, everything in the state of the generator function
freezes, and the value is returned. When the generator is called again with next(), it picks back up
right where it stopped at yield from before.
"""


def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        n = output
        i += 1


def main():
    # Test block
    my_gen = fact_gen()
    num = 5

    for i in range(num):
        print(next(my_gen))

    # Correct result when num = 5:
    # 1
    # 2
    # 6
    # 24
    # 120


if __name__ == '__main__':
    main()
