def main():
    """
      variable - container that stores a value. container is a section in
                 the computers memory.

        ex: color = "blue"

        Rules to Naming Variables:
          * cannot start with a number
            - ex: 5color = "blue" 
          * cannot contain any special characters other than underscores (_)
            - ex: $^color = "blue"
          * cannot contain any spaces
            - ex: favorite color = "blue"
    """
    x = 5
    y = "AlgoExpert"
    x = y
    z = 5
    print(z) 
    print(y) 
    print(x) 


if __name__ == "__main__":
  main()