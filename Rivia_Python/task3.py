"""
Given the participants' score sheet for your University Sports
Day, you are required to find the runner-up score. You are given
a list of scores. Determine the score of the runner-up
and display to screen.

NOTE: You can use a built-in function
"""

def main():
    input_scores = input('Please enter the scores separated by spaces here: ').split()
    
    try:
        int_scores = list(map(int, input_scores))
    except ValueError as ve:
        print(f"{ve}")
    else:
        print(f"The runner up score was: {get_runner_up(int_scores)}")


def get_runner_up(scores):
    scores.sort()
    return scores[-2]


if __name__ == '__main__':
    main()

