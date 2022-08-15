def get_unique_words(list_of_words):
    unique_words = []

    for word in list_of_words:
        if list_of_words.count(word) == 1:
            unique_words.append(word)

    return unique_words


def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    results = []

    while unique_words:  # could stop processing after n words len(results) < n
        longest_idx = 0

        for i, word in enumerate(unique_words):
            if len(word) > len(unique_words[longest_idx]):
                longest_idx = i
        results.append(unique_words.pop(longest_idx))

    return results[:n]


def main():
    """
    words = [
        "Longer",
        "Whatever",
        "Longer",
        "Ball",
        "Rock",
        "Rocky",
        "Rocky"
    ]
    """

    words = ["Hello", "Hello", "Hello", "Abcd", "bcd", "a", "ab"]

    """
    words = [
            "Hello",
            "AlgoExpert",
            "Algo",
            "Testing",
            "Programming",
            "Programming",
            "Coding",
            "Python",
            "JavaScript",
            "Coding",
            "Ruby",
        ]
    """

    n = 2

    longest_unique_words = get_n_longest_unique_words(words, n)
    print(longest_unique_words)


if __name__ == "__main__":
    main()
