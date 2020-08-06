def grid_to_string(grid, player):
    string = ''
    row = player.row
    col = player.col
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if k == col and i == row:
                string += player.display
            else:
                string += str(grid[i][k].display)
        string += "\n"
    if player.num_water_buckets != 1:
        string += "\nYou have {} water buckets.".format(player.num_water_buckets)
    else:
        string += "\nYou have {} water bucket.".format(player.num_water_buckets)
    return string 

