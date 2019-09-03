"""
    1. Ask the user to enter a fruit, keep doing this until they enter the letter q.
    2. Print all fruits enter on a single line in alphabetical order.
"""


def main():
    fruit_basket = []

    while True:
        fruit = input("Please enter the name of a fruit and I will add it to your basket. (type 'q' to exit): ")
        if fruit.lower() == 'q':
            break
        fruit_basket.append(fruit)

    if fruit_basket:
        for f in sorted(fruit_basket):
            print(f"{f}", end=' ')


if __name__ == '__main__':
    main()
