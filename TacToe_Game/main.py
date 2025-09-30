from grid_creation import GridCreation
from player import Player

def main():

    grid_obj = GridCreation()
    player_obj = Player()

    turn = True  # Start with player1
    moves = 0

    while moves < 9:
        grid_obj.print_grid()
        player_obj.player_turn(turn)

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        symbol = "X" if turn else "O"
        if grid_obj.move(row, col, symbol):
            moves += 1
            if player_obj.check_winner(grid_obj.grid, symbol):
                grid_obj.print_grid()
                winner = player_obj.player1 if turn else player_obj.player2
                print(f"{winner} wins!")
                return
            turn = not turn

    grid_obj.print_grid()
    print("It is a draw!")

if __name__ == "__main__":
    main()