
class GridCreation:

    def __init__(self):
        # initialize grid when the object is created
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

      
    def grid_board(self):
            return self.grid


    #grid printing
    def print_grid(self):
        for i in range(3):
            print("|", end ="")
            for j in range(3):
                print (self.grid[i][j], "|", end ="")
            print("")



    def move(self, row, col, symbol):
        if self.grid[row][col] == " ":
              self.grid[row][col] = symbol
              return True
        else:
             print("Cell is already taken! Try again.")
             return False
             
