from collections import deque
def do_move(valid_moves, notebook):    
    new_move= ()
    if len(valid_moves)==1:    
        new_move=(dict.get("x"), dict.get("y")) 
        valid_moves.remove(dict)
        notebook.append(dict)

    if len(valid_moves)==2 and dict[exit] == "yes":
        new_move =(dict.get("x"), dict.get("y"))
    if len(valid_moves)>= 2:                

        if dict[type]== "normal":
            new_move =(dict.get("x"), dict.get("y"))
            valid_moves.remove(dict)
            notebook.append(dict)                 
            
        else:
            try_dict=valid_moves[0]
            new_move=((try_dict.get("x"), try_dict.get("y")))
            valid_moves.remove(dict)
            notebook.append(dict) 
                
        
    
    return new_move, notebook