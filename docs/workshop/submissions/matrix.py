#aggiungere più cose possibili in notebook: wrong_paths, visited, visitable.
#visited[-1], if len(adjacent_room) = 0

#not_mud = []
#for el in adjacent:
#   if el["players"] != set()
#   visitable.append(el["x"], el["y"])
#   else: 
#       if el["type"] == normal
#   not_mud


def do_move(valid_moves, notebook):
    notebook["normal"] = []
    notebook["mud"] = []
    if len(notebook) == 2:
        notebook["visited"] = []
    if len(notebook) > 2: 
        notebook["wrong_list"] = []
    for el in valid_moves:
        if el["exit"] == "yes":
            new_move = (el["x"], el["y"])
            notebook = {}
        else:
            if el["type"] == "normal":
                if(el["x"], el["y"]) not in notebook["normal"]:
                    notebook["normal"].append((el["x"], el["y"]))    
            elif el["type"] == "mud":
                if(el["x"], el["y"]) not in notebook["mud"]:
                    notebook["mud"].append((el["x"], el["y"]))
    if el not in notebook["visited"]:
        if len(notebook["normal"]) > 0:
            new_move = notebook["normal"][0]
            notebook["visited"].append(new_move)
        elif len(notebook["mud"]) > 0 and len(notebook["normal"]) == 0: 
            new_move = notebook["mud"][0]
            notebook["visited"].append(new_move)
    else:
        new_move = notebook["visited"][-1] 
        notebook["visited"].remove(notebook["visited"][-1])
        notebook["visited"].append(new_move)
    #print(notebook)
    return new_move, notebook
