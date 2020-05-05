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

    # print(check_sudoku(correct))
    # >>> True

    # print(check_sudoku(incorrect2))
    # >>> False

    # print(check_sudoku(incorrect3))
    # >>> False

    # print(check_sudoku(incorrect4))
    # >>> False

    # print(check_sudoku(incorrect5))
    # >>> False


def check_sudoku(entries):
    for row in entries:
        results = list(range(1, len(entries[0]) + 1))
        for i in row:
            if i not in results:
                return False
        results.remove(i)
    for n in range(len(entries[0])):
        results = list(range(len(entries[0])))
        for row in entries:
            if row[n] not in results:
                return False
        results.remove(row[n])
    return True


if __name__ == '__main__':
    main()
