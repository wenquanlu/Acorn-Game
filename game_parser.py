from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


start = Start()
end = End()
air = Air()
wall = Wall()
fire = Fire()
water = Water()


def read_lines(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return parse(lines)

        #Read in a file, process them using parse(),
        #and return the contents as a list of list of cells.

    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()



def parse(lines):
    ls = []
    i = 0 
    x_time = 0
    y_time = 0
    # Use a list to count paired teleports
    pile_up_teleport = [0,0,0,0,0,0,0,0,0]
    while i < len(lines):
        k = 0 
        one_line = []

        while k < len(lines[i]):
            if lines[i][k] == 'X':
                x_time += 1
                one_line.append(start)
            elif lines[i][k] == 'Y':
                y_time += 1
                one_line.append(end)
            elif lines[i][k] == ' ':
                one_line.append(air)
            elif lines[i][k] == '*':
                one_line.append(wall)
            elif lines[i][k] == 'F':
                one_line.append(fire)
            elif lines[i][k] == 'W':
                one_line.append(water)
            elif lines[i][k].isdigit() == True and int(lines[i][k]) > 0 and int(lines[i][k]) < 10:
                one_line.append(Teleport(int(lines[i][k])))
                pile_up_teleport[int(lines[i][k])-1] += 1
            elif not (lines[i][k] == '\n' or (i == len(lines)-1 and k == len(lines[i])-1)):
                raise ValueError("Bad letter in configuration file: {}.".format(lines[i][k]))
            if lines[i][k] == '\n' or (i == len(lines)-1 and k == len(lines[i])-1):
                ls.append(one_line)
            
            k += 1
        i += 1
    if x_time>1:
        raise ValueError("Expected 1 starting position, got {}.".format(x_time))
    if x_time==0:
        raise ValueError("Expected 1 starting position, got 0.")
    if y_time>1:
        raise ValueError("Expected 1 ending position, got {}.".format(y_time))
    if y_time==0:
        raise ValueError("Expected 1 ending position, got 0.")
    j = 0
    while j < len(pile_up_teleport):
        if not (pile_up_teleport[j] == 2 or pile_up_teleport[j] == 0):
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(j+1))
        j += 1
    return ls

