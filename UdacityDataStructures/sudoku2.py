"""Sudoku class for interacting with elements of a Sudoku puzzle."""


class Sudoku:
    def __init__(self, row_length: int, column_length: int):
        """Sudoku object initialization."""
        self.row_length: int = row_length
        self.column_length: int = column_length

    def is_valid_answer(self, answers: list) -> bool:
        """Validates answers to a Sudoku puzzle of size n x n.

        :param answers: nested list of size n x n
        :type answers: list of integers
        :return: returns True or False
        :rtype: bool
        """
        # loop over each nested list in our answers list
        for row_list in answers:
            # calculate row expected values
            row_expected_answers: list = list(range(1, self.row_length + 1))

            # loop over current list and check for membership
            for num in row_list:
                if num not in row_expected_answers:
                    return False
                row_expected_answers.remove(num)

        # loop over each nested list in our answers list
        for r_data in answers:
            # calculate column expected values
            column_expected_answers: list = list(range(1, self.column_length + 1))

            # loop over each index and check all rows for proper membership
            # (row 00, then 10, then 20, ...)
            for i in range(self.column_length):
                if r_data[i] not in column_expected_answers:
                    return False
                column_expected_answers.remove(r_data[i])
        return True

    def is_valid_size(self, answers: list) -> bool:
        """Confirms the size expected is the actual size passed."""
        c_size: int = len(answers)
        r_size: int = len(answers[0])

        if c_size != self.column_length or r_size != self.row_length:
            return False
        return True


if __name__ == '__main__':
    import sys

    # fails
    test_list = [
        [1, 2, 3, 4],
        [2, 1, 4, 3],
        [3, 4, 1, 2],
        [4, 3, 2, 2],
    ]

    # passes
    test_list2 = [
        [1, 2, 3, 4],
        [2, 1, 4, 3],
        [3, 4, 1, 2],
        [4, 3, 2, 1],
    ]
    test_cases = [test_list, test_list2]

    sudoku = Sudoku(4, 4)
    for j in range(len(test_cases)):
        if sudoku.is_valid_size(test_cases[j]):
            if sudoku.is_valid_answer(test_cases[j]):
                print(f"Test Case {j+1} - Sudoku answers are correct.")
                print("-" * 8)
                for row in test_cases[j]:
                    for r in row:
                        print(r, end=" ")
                    print()
            else:
                print(f"Test Case {j+1} - Sudoku answers are incorrect.")
                continue
        else:
            print("ERROR: Could not validate Sudoku puzzle size...exiting")
            sys.exit(1)
