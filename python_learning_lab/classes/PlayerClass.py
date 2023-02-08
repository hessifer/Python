class Player:
    # class variable
    number_of_players = 0

    # constructor or init method
    # init method is automatically run when you create an instance
    # of the class
    def __init__(self, player_handle):
        self.player_handle = player_handle
        self.id = 1
        Player.number_of_players += 1

    def greeting(self):
        return "Welcome to the Player class."


if __name__ == "__main__":
    # create an instance of the Player class
    player1 = Player("Nagalot")
    player2 = Player("Lone")

    # print the value of an instance variable and
    # call an instance method
    print(f"{player1.greeting()} - {player1.player_handle}")
    print(f"{player2.greeting()} - {player2.player_handle}")

    print(f"{Player.number_of_players}")
