def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


def main():
    lessons = ["Why Python Programming", "Data Types and Operators",
               "Control Flow", "Functions", "Scripting"]

    for i, lesson in my_enumerate(lessons, 1):
        print("Lesson {}: {}".format(i, lesson))


if __name__ == "__main__":
    main()
