from birthday import Birthday

def main():
    birth_year = input("Enter the four digit year you were born (yyyy): ")
    birth_month = input("Enter the two digit month you were born (mm): ")
    birth_day = input("Enter the two digit day you were born (dd): ")
    try:
        my_birthday = Birthday(birth_year, birth_month, birth_day)
    except ValueError as ve:
        print(f"ERROR exiting...{ve}")

    print(f"It has been {my_birthday.days_since_birth():,} days since you were born.")


if __name__ == '__main__':
    main()