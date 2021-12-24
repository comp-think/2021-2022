# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to solve the maze.

from collections import deque
from os import X_OK

def do_move(valid_moves, notebook):
    note = deque(notebook)

    if len(valid_moves) == 1:
        currentMove = valid_moves.pop()
        futX = currentMove.get("x")
        futY = currentMove.get("y")
        new_move = (futX, futY)
        note.append(new_move)

    else:
        for el in valid_moves:
            if (el.get("x"), el.get("y")) in note:
                valid_moves.remove(el)
        currentMove = valid_moves.pop()
        futX = currentMove.get("x")
        futY = currentMove.get("y")
        new_move = (futX, futY)
        note.append(new_move)

    #print(new_move)   
    #print(notebook) 
    
    return new_move, note