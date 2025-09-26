from grid_creation import GridCreation
from player import Player

def main():

    grid_obj = GridCreation()
    print(grid_obj.grid_board())

    grid_obj.print_grid()

    player_obj = Player()
    turn = True  # Start with player1
    player_obj.player_turn(turn)

if __name__ == "__main__":
    main()