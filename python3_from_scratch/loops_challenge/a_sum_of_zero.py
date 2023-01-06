def main() -> None:
    num_list = [10, -14, 26, 5, -3, 13, -5]

    print(check_sum(num_list))


def check_sum(num_list: list) -> bool:
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