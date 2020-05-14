def main():
    correct = [[1, 2, 3],
               [2, 3, 1],
               [3, 1, 2]]

    incorrect = [[1, 2, 3, 4],
                 [2, 3, 1, 3],
                 [3, 1, 2, 3],
                 [4, 4, 4, 4]]

    incorrect2 = [[1, 2, 3, 4],
                  [2, 3, 1, 4],
                  [4, 1, 2, 3],
                  [3, 4, 1, 2]]

    incorrect3 = [[1, 2, 3, 4, 5],
                  [2, 3, 1, 5, 6],
                  [4, 5, 2, 1, 3],
                  [3, 4, 5, 2, 1],
                  [5, 6, 4, 3, 2]]

    incorrect4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    incorrect5 = [[1, 1.5],
                  [1.5, 1]]

    print(check_sudoku(incorrect))
    # >>> False

    print(check_sudoku(correct))
    # >>> True

    print(check_sudoku(incorrect2))
    # >>> False

    print(check_sudoku(incorrect3))
    # >>> False

    print(check_sudoku(incorrect4))
    # >>> False

    print(check_sudoku(incorrect5))
    # >>> False


def check_sudoku(entries):
    # loop over entries iterator (nested list).
    # row represents a list during each iteration

    # examine the contents of each row first to confirm
    # each expected value is present in the row list.
    # If not return False and we are done.
    for row in entries:
        expected_values = list(range(1, len(entries[0]) + 1))

        for number in row:
            if number not in expected_values:
                return False
            expected_values.remove(number)

    # create an iterator using the generator range() and
    # iterate over it, the iteration count is based on
    # the size of our function argument 'entries'

    # loop over each nested list
    for i in range(len(entries[0])):
        # create our expected_values list and populate it with
        # each value from 0 to the length of the first element (list)
        # minus 1 (using range) of the entries argument.
        expected_values = list(range(1, len(entries[0]) + 1))  # [1, 2, 3, 4]

        for row in entries:
            if row[i] not in expected_values:
                return False
            expected_values.remove(row[i])
    return True


if __name__ == '__main__':
    main()
