"""
Learning Objectives
    * Demonstrate understanding of basic Python tools, including using
      syntax basics, defining variables, and accepting user input.
    * Explain basic Python data types and describe the differences
      between each data type.
    * Use numbers and number operations in a Python application.
    * Use Boolean values in Python application, especially in the use
      of conditional statements.
    * Use conditional statements to determine the outcome of a program.
"""

"""
Tax Rates
    10%                 Up to $9,875.00
    12%                 $9,876.00 to $40,125.00
    22%                 $40,126.00 to $85,525.00
    24%                 $85,526.00 to $163,300.00
    32%                 $163,301.00 to $207,350.00
    35%                 $207,351.00 to $518,400.00
    37%                 $518,401.00 or more
"""

"""
inputs
    * gross income entered to nearest cent (float)
    * number of dependents (int)
"""

"""
Notes:
    * all taxpayers are allowed a $12,200.00 standard deduction
    * for each dependent, a taxpayer is allowed an additional $2,000 deductions
"""


def menu() -> tuple:
    """
        descritpion: display menu to user and takes as input
          gross income and number of dependents and returns
          them as a tuple.

        input:
            gross income: float
            number of dependents: int
    """
    gi_text = "Please enter your gross income for the year: "
    nod_text = "Pleaase enter the number of dependents you are claiming: "
    ve_text = "ERROR: please enter the correct value type (gross_income: "
    ve_text = ve_text + "float) (number_of_dependents: int)"

    try:
        gross_income: float = float(input(gi_text))
        number_of_dependents = int(input(nod_text))
    except ValueError as ve:
        print(f"{ve_text} --> {ve}")
    else:
        return (gross_income, number_of_dependents)


if __name__ == "__main__":
    gross_income, dependents = menu()
