from grid import grid_to_string
from game import Game
import sys
if len(sys.argv) != 3:
    print("Usage: python3 solver.py <filename> <mode>")
    exit()

filename = sys.argv[1]
mode = sys.argv[2]

# This function compares two game states
def equal_game_states(game1,game2):
    i = 0
    while i < len(game1.grid_object):
        j = 0
        while j < len(game1.grid_object[i]):
            if type(i) != type(j):
                return False
            j += 1
        i += 1
    if game1.player_object.row == game2.player_object.row and \
        game1.player_object.col == game2.player_object.col and\
        game1.player_object.num_water_buckets == game2.player_object.num_water_buckets:
        return True
    else:
        return False
# This function prevents the acorn from roasting to death by checking number of water buckets and fire
def valid(game,move):
    row = game.player_object.row
    col = game.player_object.col  
    if game.player_object.num_water_buckets == 0:
        if move == "s" and game.grid_object[row+1][col].display == "F":
            return False
        elif move == "w" and game.grid_object[row-1][col].display == "F":
            return False
        elif move == "a" and game.grid_object[row][col-1].display == "F":
            return False
        elif move == "d" and game.grid_object[row][col+1].display == "F":
            return False
        else:
            return True
    else:
        return True


def find_end(gamei):
    if gamei.grid_object[gamei.player_object.row][gamei.player_object.col].display == "Y":
        return True
    else:
        return False

def fast_forward(game,ls):
    i = 0
    while i < len(ls):
        game.game_move(ls[i])
        i += 1
# This function checks if the current game is already in the visited game states
def in_game_states(game,game_states):
    i = 0 
    while i < len(game_states):
        if equal_game_states(game,game_states[i]):
            return True
        i += 1
    return False


possible_move = ["w","a","s","d","e"]
def solve(mode):
    game_setup = Game(filename)
    if mode == "DFS":
        visited_game_states = [game_setup]
        stack = [game_setup]
        while True:
            in_gamestates = True
            i = 0
            while i < len(possible_move):
                game = Game(filename)
                fast_forward(game,stack[-1].moves)
                if valid(game,possible_move[i]) == True:
                    game.game_move(possible_move[i])
                    if in_game_states(game,visited_game_states) == False:
                        in_gamestates = False
                        visited_game_states.append(game)
                        stack.append(game)
                        break
                i += 1
            if in_gamestates == True:
                stack.pop(-1)
            if find_end(game) == True:
                print("Path has {} moves.".format(len(game.moves)))
                print("Path: {}".format(", ".join(game.moves)))
                return
            if len(stack) == 0:
                print("There is no possible path.")

    if mode == "BFS":
            visited_game_states = [game_setup]
            stack = [game_setup]
            while True:
                in_gamestates = True
                i = 0
                while i < len(possible_move):
                    game = Game(filename)
                    fast_forward(game,stack[0].moves)
                    if valid(game,possible_move[i]) == True:
                        game.game_move(possible_move[i])
                        if in_game_states(game,visited_game_states) == False:
                            in_gamestates = False
                            visited_game_states.append(game)
                            stack.append(game)
                            break
                    i += 1
                if in_gamestates == True:
                    stack.pop(0)
                if find_end(game) == True:
                    print("Path has {} moves.".format(len(game.moves)))
                    print("Path: {}".format(", ".join(game.moves)))
                    return
                if len(stack) == 0:
                    print("There is no possible path.")
                    return

if __name__ == "__main__":
    solve(mode)

