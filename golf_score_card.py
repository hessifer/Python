import sys
import os


def main():
    # DONE: top level menu to add a round of golf,
    # DONE: implement option 1
    # TODO: implement option 2
    # DONE: implement option 3
    golf_score_book = {'frasch': {'charles': []}}  # course, player, scores

    while True:
        clear_screen()
        menu(golf_score_book)


def menu(score_db):
    menu_banner = "** Welcome to the Golf Score Card **"
    menu_option1 = "1.) Add a round of golf"
    menu_option2 = "2.) Calculate Average Round of Golf"
    menu_option3 = "3.) Quit"
    
    print(f"{menu_banner}\n{menu_option1}\n{menu_option2}\n{menu_option3}\n")
    answer = int(input("\n> "))

    if answer == 3:
        sys.exit()
    if answer == 1:
        name = input("Enter Player Name: ")
        add_round(score_db, name)
    print(f"{score_db}")


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
    # check if 5 rounds have been played
    pass


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


if __name__ == "__main__":
    main()
