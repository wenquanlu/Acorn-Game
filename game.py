from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

class Game:
    def __init__(self, filename):
        self.filename = filename
        # initialise player using initialise method 
        self.grid_object = read_lines(self.filename)
        self.player_object = self.initialise()
        self.moves = []
    def game_move(self, move):
        self.player_object.move(move)
        self.moves.append(move)
        if self.player_object.touch_boundary == True:
            self.player_object.touch_boundary = False
            self.moves.pop(-1)
            return ("\nYou walked into a wall. Oof!")
        if self.grid_object[self.player_object.row][self.player_object.col].display\
            in ["X","Y"," ","W","F","*"] or\
            type(self.grid_object[self.player_object.row][self.player_object.col].display) == int:
            return self.grid_object[self.player_object.row][self.player_object.col].step(self)
    # This initialises the player's initial coordinate 
    def initialise(self):
        i = 0
        player = Player()
        while i < len(self.grid_object):
            j = 0 
            while j < len(self.grid_object[i]):
                if self.grid_object[i][j].display == "X":
                    player.row = i
                    player.col = j
                j += 1
            i += 1
        # initialise player's attribute list of cells
        player.list_of_cells = self.grid_object
        return player


