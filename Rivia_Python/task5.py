"""
You work for LSU and have been tasked with identifing how many students enrolling
speak both english and french. Using the set data type display to the screen the number
of students who speak both english and french.
"""

def main():
    english_speakers = {1, 2, 3, 4}
    french_speakers = {6, 10, 3, 9}
    dual_speakers = english_speakers.intersection(french_speakers)

    print(f"There are {len(dual_speakers)} student(s) enrolling that speak both English and French.")


if __name__ == '__main__':
    main()