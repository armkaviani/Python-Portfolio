
class Player:
    def __init__(self):
            self.player1 = input("Please enter name of player 1 : ")
            self.player2 = input("Please enter name of player 2 : ")


    def player_turn(self, turn_player1):
        if turn_player1:
            print(f"It's {self.player1}'s turn (X)")
        else:
            print(f"It's {self.player2}'s turn (O)")

    
    def check_winner(grid, symbol):
        # Check rows
        for row in grid:
            if all(cell == symbol for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(grid[row][col] == symbol for row in range(3)):
                return True
        # Check diagonals
        if all(grid[i][i] == symbol for i in range(3)):
            return True
        if all(grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False
