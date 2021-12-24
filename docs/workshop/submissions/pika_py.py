# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to solve the maze.

def do_move(valid_moves, notebook):
    maximum_move = 25
    my_position = (1, 0)
    new_move = None
    for move in valid_moves:
        x = move["x"]
        y = move["y"]
        my_tuple = (x, y)
        notebook["my_move"] = []
        if my_tuple not in notebook["my_move"]:
            if move["exit"] == "yes":
                pass #print("you won")
            else:
                if move["type"] == "normal":
                    new_move = (move["x"], move["y"])
                else:
                    new_move = (move["x"], move["y"])
            my_position = new_move
            notebook["my_move"] = my_tuple
    maximum_move = maximum_move - 1
    #print(new_move)
    #print(maximum_move)
    #print(my_position)
    return new_move, notebook

