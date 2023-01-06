def main() -> None:
    num_list_1 = [10, -14, 26, 5, -3, 13, -5]
    num_list_2 = [10, -14, 26, 5, -3]

    print(f"Test 1: {check_sum(num_list_1)}")
    print(f"Test 2: {check_sum(num_list_2)}")


def check_sum(num_list: list) -> bool:
    """
    You must implement the check_sum() function which takes in a list and
    returns True if the sum of two numbers in the list is zero. If no such
    pair exists, return False.
    """
    num_list_len = len(num_list)

    if num_list_len <= 0:
        return False

    for i in range(num_list_len):
        for j in range(i+1, num_list_len):
            if num_list[i] + num_list[j] == 0:
                return True
    return False


if __name__ == "__main__":
    main()
