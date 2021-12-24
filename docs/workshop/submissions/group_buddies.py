from collections import deque
def do_move(valid_moves, notebook):
    result=None
    possible_moves=deque()
    possible_moves.extend(valid_moves)
    if possible_moves:
        new_move=possible_moves.popleft()
        new_pos=(new_move.get["x"], new_move.get["y"])
        notebook.add(new_move) 

    else: 
        back_move=notebook.pop()
        new_pos=(back_move.get["x"], back_move.get["y"])

    while result==None:
        if new_move.get["exit"] == "yes":
            result = (new_pos, notebook)

        if new_move.get["type"] == "mud":
            result = (new_pos, notebook)
        else:
            new_pos = do_move(valid_moves, notebook) 
            result = (new_pos, notebook)
            
    return result