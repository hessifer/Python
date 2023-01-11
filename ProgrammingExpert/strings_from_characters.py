"""
Write a function that accepts a dictionary called frequencies and two strings
named string1 and string2. The frequencies dictionary contains character
keys and integer values, the value associated with each character 
represents its frequency. Your function should return 0, 1, or 2 according
to the cases below.

 - Your function should return 2 if the frequency of characters in the
   dictionary is sufficient to create both string1 and string2 without
   reusing any characters.

 - Your function should return 1 if the frequency of characters in the
   dictionary is sufficient to create either string1 or string2 without 
   reusing any characters.

 - Your function should return 0 if the frequency of characters in the
   dictionary is not sufficient to create either string1 or string2
   without reusing any characters.
"""

def main() -> None:
    sample_input_dict = {
        "h": 2,
        "e": 1,
        "l": 1,
        "r": 4,
        "a": 3,
        "o": 2,
        "d": 1,
        "w": 1,
    }

    sample_input_dict2 = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
    sample_input_dict3 = {"a": 3, "b": 1, "c": 3, "d": 2, "e": 1} 

    string1 = "hello"
    string2 = "world"
    string3 = "aaabbbc"
    string4 = "bbccde"

    # if both words are missing 1 or more chars from dict, return 0
    # check each string to see if we have enough chars for 1 or both, return 1
    # or 2 respectively

    print(create_strings_from_characters(sample_input_dict, string1, string2))
    print(create_strings_from_characters(sample_input_dict2, string1, string2))
    print(create_strings_from_characters(sample_input_dict3, string3, string4))


def create_strings_from_characters(frequencies, string1, string2) -> int:
    if len(string1) == 0 and len(string2) == 0:
        return 2
    elif len(frequencies) == 0:
        return 0
    
    string1_dict = build_char_dict(string1) 
    string2_dict = build_char_dict(string2)
    is_string1_built = False
    is_string2_built = False
    is_both = False

    # build char dictionary
    for k,v in string1_dict.items():
        if k in frequencies.keys():
            if string1_dict[k] <= frequencies[k]:
                is_string1_built = True
            else:
                is_string1_built = False
                break
        else:
            is_string1_built = False

    # build char dictionary
    for k,v in string2_dict.items():
        if k in frequencies.keys():
            if string2_dict[k] <= frequencies[k]:
                is_string2_built = True
            else:
                is_string2_built = False
                break
        else:
            is_string2_built = False
    
    if is_string1_built and is_string2_built:
        # check to see if there are enough chars for both
        for c in string1:
            if c in string2:
                # OPTIMIZE: if you have processed letter below already, skip processing (i.e. 'l')
                if string1.count(c) + string2.count(c) <= frequencies[c]: # error here if char is in dict, does it exist in both words, if so enough to make both words, or just one
                    is_both = True
                else:
                    is_both = False
                    break
    elif is_string1_built or is_string2_built:
        is_both = False

    if is_both:
        return 2
    elif is_string1_built or is_string2_built:
        return 1

    return 0 # default to no words


def is_chars_present(word, chars_dict) -> bool:
    result = False

    for char in word:
        if char not in chars_dict:
            result = False
        else:
            result = True
    return result


def build_char_dict(word) -> dict:
    word_dict = dict()

    for char in word:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    return word_dict


if __name__ == "__main__":
    main()
