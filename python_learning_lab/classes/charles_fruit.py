"""
    1. create a fruit_basket list
    2. prompt user to enter in fruit or 'q' to quit
    3. check if fruit was entered, if so add fruit to fruit_basket list and then ask again for another fruit.
    4. if 'q' was entered end program and display fruits in alphabetically order provided there is at least 1 fruit.
"""


def main():
    fruit_basket = []

    while True:
        fruit = input("Please enter a fruit or 'q' to quit: ")

        if fruit.lower() == 'q':
            break
        fruit_basket.append(fruit)

    if len(fruit_basket) > 0:
        for f in sorted(fruit_basket):
            print(f"{f}", end=' ')


if __name__ == "__main__":
    main()
