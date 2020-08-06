from game import Game
import os
import sys
from grid import grid_to_string

if len(sys.argv) == 1:
    exit()
filename = sys.argv[1]
game = Game(filename)
print(grid_to_string(game.grid_object,game.player_object))
while True:
    raw_move = input("\nInput a move: ")
    move = raw_move.lower()
    if move == "q":
        print("\nBye!")
        exit()
    message  = game.game_move(move)
    if message == "\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the \
Honourable Furious Forest Throne, restoring your hometown back to its former \
glory of rainbow and sunshine! Peace reigns over the lands.":
        print(grid_to_string(game.grid_object,game.player_object))
        print(message)
        if len(game.moves) != 1:
            print("\nYou made {} moves.".format(len(game.moves)))
            print("Your moves: {}".format(', '.join(game.moves)))
        else:
            print("\nYou made 1 move.")
            print("Your move: {}".format(', '.join(game.moves)))
        print("\n=====================\n====== YOU WIN! =====\n=====================")
        exit()


    elif message == "\nYou walked into a wall. Oof!":
        print(grid_to_string(game.grid_object,game.player_object))
        print(message)



    elif message == "\nWhoosh! The magical gates break Physics as we know it \
and opens a wormhole through space and time.":
        print(grid_to_string(game.grid_object,game.player_object))
        print(message)


    elif message == "\n\nYou step into the fires and watch your dreams disappear :(.":
        print(grid_to_string(game.grid_object,game.player_object))
        print(message)
        print("\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of \
ash and is scattered to the winds by the next storm... You have been roasted.")
        if len(game.moves) != 1:
            print("\nYou made {} moves.".format(len(game.moves)))
            print("Your moves: {}".format(', '.join(game.moves)))
        else:
            print("\nYou made 1 move.")
            print("Your move: {}".format(', '.join(game.moves)))
        print("\n=====================\n===== GAME OVER =====\n=====================")
        exit()
    
    elif message == "\nWith your strong acorn arms, you throw a water bucket at the fire. \
You acorn roll your way through the extinguished flames!":
        print(grid_to_string(game.grid_object,game.player_object))
        print(message)

    elif message == "\nThank the Honourable Furious Forest, you've found a bucket of water!":
        print(grid_to_string(game.grid_object,game.player_object))
        print(message)
        

    elif message == None:
        print(grid_to_string(game.grid_object,game.player_object))


    if move != "w" and move != "a" and move != "s" and move != "d" and move != "e" and move != "q":
        print("\nPlease enter a valid move (w, a, s, d, e, q).")
        game.moves.pop(-1)




