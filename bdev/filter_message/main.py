def filter_messages(messages):
    # messages is a list of strings

    # lists we will return
    dang_filter = []
    dang_count_by_index = []

    # loop over each message and split the 
    # words in the message to a new list
    for message in messages:
        str_list = message.split()
        count = 0

        # enumerate the new list and check for "dang"
        # remove it from the new list and increment
        # counter by 1
        for i, word in enumerate(str_list):
            if word == "dang":
                count += 1
                str_list.pop(i)
        # join the strings of the new list and
        # append them to our list of messages and
        # add the number of dang occurrences
        # to our list
        dang_filter.append(' '.join(str_list))
        dang_count_by_index.append(count)

    return dang_filter, dang_count_by_index


if __name__ == "__main__":
    messages = ["hello dang", "dang hello dang", "hello hello"]
    dang_filter, dang_count_by_index = filter_messages(messages)

    print(dang_filter)
    print(dang_count_by_index)
