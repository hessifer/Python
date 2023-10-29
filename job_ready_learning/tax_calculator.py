import sys


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
Tax Rates               Single
    10%                 Up to $11,600.00
    12%                 $11600.01 to $47,150.00
    22%                 $47,150.01 to $100,525.00
    24%                 $100,525.01 to $191,950.00
    32%                 $191,950.01 to $243,725.00
    35%                 $243,725.01 to $609,350.00
    37%                 $609,350.01 or more

Tax Rates               Married Filing Jointly
    10%                 Up to $23,200.00
    12%                 $23,200.01 to $94,300.00
    22%                 $94,300.01 to $201,050.00
    24%                 $201,050.01 to $383,900.00
    32%                 $383,900.01 to $487,450.00
    35%                 $487,450.01 to $731,200.00
    37%                 $731,200.01 or more

Tax Rates               Head of Household
    10%                 Up to $16,550.00
    12%                 $16,550.01 to $63,100.00
    22%                 $63,100.01 to $100,500.00
    24%                 $100,500.01 to $191,950.00
    32%                 $191,950.01 to $243,700.00
    35%                 $243,700.01 to $609,350.00
    37%                 $609,350.01 or more
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

STANDARD_DEDUCTION: float = 12200.00
ADDITIONAL_DEDUCTION_PER_DEPENDENT: float = 2000.00


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
    filing_response = ""

    try:
        gross_income: float = float(input(gi_text))
        number_of_dependents = int(input(nod_text))
    except ValueError as ve:
        print(f"{ve_text} --> {ve}")
    else:
        print("What is your filing status?")
        print("(a) Married Filing Jointly")
        print("(b) Single")
        print("(c) Head of Household")
        filing_response = input("Enter filing status [a/b/c]: ")

        if filing_response.lower() == "a":
            filing_status = "mfj"
        elif filing_response.lower() == "b":
            filing_status = "single"
        elif filing_response.lower() == "c":
            filing_status = "hoh"
        else:
            sys.exit("ERROR: Invalid filing status entered!")

        return (gross_income, number_of_dependents, filing_status)


def calculate_taxable_income(gross_income, number_of_dependents):
    """
    description: function to calculate taxable income. takes gross
        income and number of dependents as input. The formula used
        to calculate the taxable income is:
        gross_income - STANDARD_DEDUCTION - (ADDITIONAL_DEDUCTION_PER_DEPENDENT
        * number_of_dependents)

    input:
        gross_income: float
        number_of_dependents: int

    returns:
        taxable_income: float
    """

    return gross_income - STANDARD_DEDUCTION -\
        (ADDITIONAL_DEDUCTION_PER_DEPENDENT * number_of_dependents)


if __name__ == "__main__":
    gross_income, dependents, filing_status = menu()
    taxable_income = calculate_taxable_income(gross_income, dependents)
    print(taxable_income)
    print(filing_status)
