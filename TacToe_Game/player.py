
class Player:
    def __init__(self):
            self.player1 = input("Please enter name of player 1 : ")
            self.player2 = input("Please enter name of player 2 : ")


    def player_turn(self, turn_player1):
        if turn_player1:
            turn_player1 = False
            print(f"It's {self.player2}'s turn")
        else:
            turn_player1 = True
            print(f"It's {self.player1}'s turn")
        return turn_player1