def main() -> None:
    string1 = ""
    string2 = ""
    string3 = "a"
    string4 = "a"
    string5 = "x"
    string6 = "y"
    string7 = "ab"
    string8 = "xy"
    string9 = "aba"
    string10 = "xyz"
    string11 = "---"
    string12 = "aaa"
    string13 = "---"
    string14 = "xyz"
    string15 = "xyzxyz"
    string16 = "toetoe"

    print(is_pattern(string1, string2))
    print(is_pattern(string3, string4))
    print(is_pattern(string5, string6))
    print(is_pattern(string7, string8))
    print(is_pattern(string9, string10))
    print(is_pattern(string11, string12))
    print(is_pattern(string13, string14))
    print(is_pattern(string14, string13))
    print(is_pattern(string15, string16))


def is_pattern(s1, s2) -> bool:
    """
      if lengths are not the same return False
      if strings are the same return True
      if strings chars are unique, and alphabetical return True

      In this coding exercise, you are asked to write the body of a
      function called detect_pattern that returns true or false
      depending upon whether two strings have the same pattern
      of characters. More precisely, two strings have the same
      pattern if they are of the same length and if two characters
      in the first string are equal if and only if the characters
      in the corresponding positions in the second string are also equal.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len != s2_len:
        return False
    elif s1 == s2:
        return True
    elif s1_len == 1:
        return True 
    elif s1[0] not in s1[1:] and s2[0] not in s2[1:]:
            return True

    for i in range(1, s1_len):
        if s1[0] == s1[i] and s2[0] == s2[i]:
            continue
        elif s1[0] != s1[i] and s2[0] == s2[i]:
            return False
        else:
            return False 

    return True 

if __name__ == "__main__":
    main()
