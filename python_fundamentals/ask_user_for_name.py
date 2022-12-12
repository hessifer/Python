def main() -> None:
    # get input from user and store value in name variable
    # provide information to the user about their name (hint: use a function)

    name = input("Please enter your name: ")
    name_length = get_length(name)

    print(f"Hello {return_title_case(name)}, you have {name_length} letters in your name.")

def get_length(a_str: str) -> int:
    # this is our letter counter
    count = 0 

    # loop over a_str (letter) and keep count
    for letter in a_str:
        count += 1 # short-hand for count = count + 1
    
    return count

def return_title_case(a_str: str) -> str:
    return a_str.title()    


if __name__ == "__main__":
    main()