from grid import grid_to_string
class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        pass


class End:
    def __init__(self):
        self.display = 'Y'

    def step(self,game):
        return("\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the \
Honourable Furious Forest Throne, restoring your hometown back to its former \
glory of rainbow and sunshine! Peace reigns over the lands.")


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        pass


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        if game.moves[-1] == "s":
            game.player_object.row -= 1
        elif game.moves[-1] == "w":
            game.player_object.row += 1
        elif game.moves[-1] == "a":
            game.player_object.col += 1
        elif game.moves[-1] == "d":
            game.player_object.col -= 1
        game.moves.pop(-1)
        return "\nYou walked into a wall. Oof!"


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        if game.player_object.num_water_buckets == 0:
            return("\n\nYou step into the fires and watch your dreams disappear :(.")
        else:
            game.player_object.num_water_buckets -= 1
            game.grid_object[game.player_object.row][game.player_object.col] = Air()
            return("\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way \
through the extinguished flames!")
        

class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        game.player_object.num_water_buckets += 1
        game.grid_object[game.player_object.row][game.player_object.col] = Air()
        return ("\nThank the Honourable Furious Forest, you've found a bucket of water!")


class Teleport:
    def __init__(self, display):
        self.display = display 

    def step(self, game):
        if game.moves[-1] == "w" or game.moves[-1] == "a" or game.moves[-1] == "s" or game.moves[-1] == "d"\
            or game.moves[-1] == "e" or game.moves[-1] == "q":
            for i in game.grid_object:
                for k in i:
                    if k.display == self.display:
                        row_of_another_teleport = game.grid_object.index(i)
                        col_of_another_teleport = i.index(k)
                        # This ensures it is another teleport, not the one player is standing on
                        if game.player_object.row != row_of_another_teleport or \
                            game.player_object.col != col_of_another_teleport:
                            game.player_object.row = row_of_another_teleport
                            game.player_object.col = col_of_another_teleport
                            return("\nWhoosh! The magical gates break Physics \
as we know it and opens a wormhole through space and time.")
        else:
            pass
            


    


