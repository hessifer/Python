def my_range(x):
    i = 0

    while i < x:
        yield i
        i += 1


def main():
    # prints generator object
    # print("{}".format(my_range(10)))
    for n in my_range(4):
        print("\n{}".format(n))


if __name__ == "__main__":
    main()
