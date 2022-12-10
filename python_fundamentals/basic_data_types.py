def main():
    # entry point of every program
    # def is the keyword used to define a function in Python
    # ideally every program has a main() function and all execution starts there.
    """
      Basic Python Data Types
      -----------------------
      - int
      - float
      - str
      - bool

      int: all integers, positive or negative with no fractional portion
        ex: ..., -3, -2, -1, 0, 1, 2, 3, ...

      float: numbers with fractional/decimal portions, positive or negative
        ex: ..., -2.1, -1.5, .2, 7., 3.14, ....
    
      str: (String) a sequence of characters. A character is a single letter like 'C'.
        ex: "hello", 'hello', '''hello''', "5", 'False'
    
      bool: binary value (two values only) True or False
        ex: True, False
    """
    data_type1 = "int"
    data_type2 = "float"
    data_type3 = "str"
    data_type4 = "bool"
    print(f"Basic Data Types in Python are: {data_type1}, {data_type2}, {data_type3}, {data_type4}") 


# if the built-in __name__ has a value of __main__ execute below code
# essentially we are calling this program directly and not through another program
if __name__ == "__main__":
    main()