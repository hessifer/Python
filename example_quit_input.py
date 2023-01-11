def main():
    answer = 'n'

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("You enter an incorrect value.")
    else:
        if age > 18:
            print("You are getting older..")
        while answer != 'q':
            answer = input("Enter (q) to quit: ")
            try:
                age = int(input("Enter your age: "))
            except ValueError:
                print("You enter an incorrect value.")
            else:
                if age > 18:
                    print("You are getting older..")
                answer = input("Enter (q) to quit: ")


if __name__ == "__main__":
    main()


    