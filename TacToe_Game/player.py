
class Player:
    def __init__(self):
            self.player1 = input("Please enter name of player 1 : ")
            self.player2 = input("Please enter name of player 2 : ")


    def player_turn(self, turn_player1):
        if turn_player1:
            print(f"It's {self.player1}'s turn (X)")
        else:
            print(f"It's {self.player2}'s turn (O)")
