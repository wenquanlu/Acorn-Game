class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        # first set to 0, the coordinate will be initialised again in game.py by finding initial position X
        self.row = 0   
        self.col = 0
        self.touch_boundary = False
        self.list_of_cells = []

    def move(self, move):
        if move == "w":
            self.row -= 1
            if self.row < 0:
                self.row += 1
                self.touch_boundary = True
        elif move == "a":
            self.col -= 1
            if self.col < 0:
                self.col += 1
                self.touch_boundary = True
        elif move == "s":
            self.row += 1
            if self.row >= len(self.list_of_cells):
                self.row -= 1
                self.touch_boundary = True
        elif move == "d":
            self.col += 1
            if self.col >= len(self.list_of_cells[0]):
                self.col -= 1
                self.touch_boundary = True
        elif move == "e":
            pass
        
        
