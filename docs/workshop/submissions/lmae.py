# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to solve the maze.
from random import choice, seed

def mean(array):
    return sum(array) // len(array)


def determine_start_position(valid_moves):
    xs = [move['x'] for move in valid_moves]
    ys = [move['y'] for move in valid_moves]


    if len(xs) == 4 and len(ys) == 4:
        return mean(xs), mean(ys)


def do_move(valid_moves, notebook):
    if len(notebook) == 0:
        notebook['path'] = []

    # print(valid_moves)

    exit_moves = [move for move in valid_moves if move['exit'] == 'yes']

    if len(exit_moves) > 0:
        # go directly to exit if there's at least one exit right now
        # no need to store this move, since this one must be the last
        exit_move = exit_moves[0]
        return (exit_move['x'], exit_move['y']), notebook
    else:
        # otherwise filter out possible (not mud) moves
        valid_moves = [move for move in valid_moves if move['type'] == 'normal']

        # filter out cells we haven't stepped into yet, no need to walk in circles
        new_moves = [move for move in valid_moves if (move['x'], move['y']) not in notebook['path']]

        if len(new_moves) > 0:
            # if there's at least one such cell, choose it
            new_move = choice(new_moves)
        else:
            # otherwise walk back, we have no other choice
            #print(valid_moves)
            new_move = choice(valid_moves)

        new_move = (new_move['x'], new_move['y'])
        notebook['path'].append(new_move)

        #print(notebook['path'])

    return new_move, notebook