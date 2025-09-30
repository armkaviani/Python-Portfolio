from grid_creation import GridCreation
from player import Player

def main():

    grid_obj = GridCreation()
    player_obj = Player()

    print(grid_obj.grid_board())

    turn = True  # Start with player1
    moves = 0

    while moves < 9:
        grid_obj.print_grid()
        player_obj.player_turn(turn)

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

if __name__ == "__main__":
    main()