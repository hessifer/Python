"""
Modify example 10 so that the file vowel_search_results.txt does not
get overwritten. Insert a blank line before each new entry in the file.

Write a program that asks the user for a file to analyze. Consider
the exceptions that may arise and handle them. Make sure to use type
annotation for your variables and return types. Once you have
the file to read, examine the contents of the file and keep a count
for each vowel found. Write the results to a file called
vowel_search_results.txt so that the output appears like:

********* Vowel Search Report - /home/hessifer/source_file **********
---------------------------------------------------------------------
Unique Vowels Found: 5
Number of Times Vowels Appear in File: 45
A Count: 12
E Count: 4
I Count: 2
O Count: 12
U Count: 15

********** Vowel Search Report - /etc/services **********
---------------------------------------------------------
Unique Vowels Found: 5
Number of Times Vowels Appear in File: 154560
A Count: 35158
E Count: 46710
I Count: 28890
O Count: 28521
U Count: 15281

"""
import sys


def main():
    """Main entry of program."""
    if len(sys.argv) == 3:
        source_file: str = sys.argv[1]
        target_file: str = sys.argv[2]
    else:
        display_help()
        sys.exit(1)

    try:
        with open(source_file) as fh:
            data = fh.read()
    except FileNotFoundError:
        print(f"ERROR: Could not locate file.")
        sys.exit(1)
    except PermissionError:
        print("ERROR: Operation not permitted.")
        sys.exit(1)

    # process data
    write_report(get_vowel_stats(data), source_file, target_file)


def get_vowel_stats(file: str) -> dict:
    """Process a file to capture statistics on vowels.

    Parameters:
    file (str): the file to process

    Returns:
    dict: Key / Value pairs {'vowel': count}

    """
    results: dict = dict()
    vowels: set = {'a', 'e', 'i', 'o', 'u'}

    for character in file:
        c = character.lower()
        if c in vowels:
            if c in results.keys():
                results[c] += 1
            else:
                results[c] = 1
    return results


def write_report(results: dict, source_file: str, report_file: str):
    """Write our report to a file.

    Parameters:
    results (dict): dictionary containing statistics on vowels found
    source_file (str): file from which statistics on vowels where generate
    report_file (str): file to write report to (truncates file)

    Returns:
    None

    """
    header_top = f"{'*' * 10} Vowel Search Report - "
    header_top += f"{source_file} {'*' * 10}"
    header_bottom = "{}".format("-" * len(header_top))
    unique_vowels_found = set(results.keys())
    total_vowels_found = sum(results.values())
    a_count = results.get('a')
    e_count = results.get('e')
    i_count = results.get('i')
    o_count = results.get('o')
    u_count = results.get('u')
    report = f"{header_top}\n{header_bottom}\nUnique Vowels Found:"
    report += f" {len(unique_vowels_found)}\nNumber of Times Vowels Appear in"
    report += f" File: {total_vowels_found}\nA Count: {a_count}\nE Count: "
    report += f"{e_count}\nI Count: {i_count}\nO Count: {o_count}\nU Count: "
    report += f"{u_count}\n"
    report += "\n"

    try:
        with open(report_file, 'a') as fh:
            fh.write(report)
    except FileNotFoundError:
        print("ERROR: No such directory.")
        sys.exit(1)
    except PermissionError:
        print("ERROR: Operation not permitted.")
        sys.exit(1)


def display_help():
    """Display usage message to screen."""
    usage_text = "usage: name_of_script.py src_file dst_file"
    print(f"{usage_text}")


if __name__ == '__main__':
    main()
