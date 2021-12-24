# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to solve the maze.

def do_move(valid_moves, notebook):
    #print(valid_moves)
    all=[]
    for i in valid_moves:
        all_moves = (i['x'], i['y'])
        all.append(all_moves)
        #new_move=all_moves
        if len(notebook)!=0:
           if all_moves not in notebook["prev"]:
               new_move=all_moves
           else:
               new_move=notebook["prev"][-1]

        else:
            new_move=all_moves
            break

    if len(notebook)==0:
        notebook['prev']=[]

    if len(notebook) != 0:
        if new_move not in notebook['prev']:
            notebook['prev'].append(new_move)

    return new_move, notebook





