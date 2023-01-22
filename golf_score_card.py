import sys
import os
import time


def main():
    golf_score_book = {'frasch': {'charles': []}}  # course, player, scores
    while True:
        clear_screen()
        menu(golf_score_book)


def menu(score_db):
    menu_banner = "** Welcome to the Golf Score Card **"
    menu_option1 = "1.) Add a round of golf"
    menu_option2 = "2.) Calculate Average Round of Golf"
    menu_option3 = "3.) Quit"
    
    print(f"\n{menu_banner}\n{menu_option1}\n{menu_option2}\n{menu_option3}\n")
    answer = int(input("\n> "))

    if answer == 3:
        sys.exit()
    if answer == 1:
        name = input("Enter Player Name: ")
        add_round(score_db, name)
    if answer == 2:
        name = input("Enter Player Name: ")
        calculate_average_round(score_db, name)
        time.sleep(3)

def add_round(golf_history, player):
    # golf_history is the dictionary of golf scores
    # player is the player's name
    # check if player has score history
    # add score or add player and score 
    player = player.lower()
    course = input("Golf Course Name: ").lower()
    score = int(input("Enter Your Score: "))

    if course in golf_history.keys():
        if player in golf_history[course].keys():
            golf_history[course][player].append(score)
        else:
            golf_history[course][player] = []
            golf_history[course][player].append(score)

    else:
        golf_history[course] = {player: []}
        golf_history[course][player].append(score)


def calculate_average_round(golf_history, player):
    player = player.lower()
    # get number of rounds played
    rounds_played = 0
    total_score = 0

    for key in golf_history.keys():
        for k in golf_history[key].keys():
            if k == player:
                rounds_played += len(golf_history[key][k])
                if rounds_played:
                     total_score += sum(golf_history[key][k])    

    # check if 5 rounds have been played
    if rounds_played < 5:
        print(f"{player.title()} has not played enough rounds. ({rounds_played}/5)")
    else:
        print(f"Your average score for {rounds_played} rounds played is {int(total_score / rounds_played)}.")

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


if __name__ == "__main__":
    main()
