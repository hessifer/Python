"""
Write a program that asks the user for a file to analyze. Consider the exceptions that may arise
and handle them. Make sure to use type annotation for your variables and return types. Once you have
the file to read, examine the contents of the file and keep a count for each vowel found. Write the
results to a file called vowel_search_results.txt so that the output appears like:

********* Vowel Search Report - /home/hessifer/source_file **********
---------------------------------------------------------------------
Unique Vowels Found: 5
Number of Times Vowels Appear in File: 45
A Count: 12
E Count: 4
I Count: 2
O Count: 12
U Count: 15
"""


def main():
    """Main entry of program."""
    source_file = input("Please enter a file to analyze > ")
    data = ""

    try:
        with open(source_file) as fh:
            for line in fh.readlines():
                data += line
    except FileNotFoundError:
        print(f"ERROR: Could not locate file.")
 
    # process data
    write_report(get_vowel_stats(data), source_file)


def get_vowel_stats(file: str) -> dict:
    """Process a file to capture statistics on vowels."""
    results = dict()
    vowels = ('a', 'e', 'i', 'o', 'u')

    for line in file:
        for word in line.strip().lower().split(" "):
            for c in word:
                if c in vowels:
                    if c in results.keys():
                        results[c] += 1
                    else:
                        results[c] = 1
    return results


def write_report(results: dict, source_file: str, report_file="vowel_search_results.txt"):
    """Takes a results dict and writes the data to a file."""
    header_top = "{} Vowel Search Report - {} {}".format("*"*10, source_file, "*"*10)
    header_bottom = "{}".format("-" * len(header_top))
    unique_vowels_found = set(results.keys())
    total_vowels_found = sum(results.values())
    a_count = results.get('a')
    e_count = results.get('e')
    i_count = results.get('i')
    o_count = results.get('o')
    u_count = results.get('u')

    with open(report_file, 'w+') as fh:
        fh.write(header_top)
        fh.write("\n")
        fh.write(header_bottom)
        fh.write("\n")
        fh.write(f"Unique Vowels Found: {len(unique_vowels_found)}")
        fh.write("\n")
        fh.write(f"Number of Times Vowels Appear in File: {total_vowels_found}")
        fh.write("\n")
        fh.write(f"A Count: {a_count}")
        fh.write("\n")
        fh.write(f"E Count: {e_count}")
        fh.write("\n")
        fh.write(f"I Count: {i_count}")
        fh.write("\n")
        fh.write(f"O Count: {o_count}")
        fh.write("\n")
        fh.write(f"U Count: {u_count}")
        fh.write("\n")


if __name__ == '__main__':
    main()
