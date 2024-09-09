def validate_path(expected_path, character_path):
    hit = 0
    percent = 0.0

    cp = character_path[1:]

    for i in range(len(cp)):
        if cp[i] == expected_path[i]:
            hit += 1

    if hit != 0:
        percent = float(hit / len(cp) * 100)

    return character_path[0], percent


if __name__ == '__main__':
    expected_path = "UDUDUDUD"
    character_path = ["A", "U", "D", "U", "D", "U", "D", "U", "D"]
    print(validate_path(expected_path, character_path))
