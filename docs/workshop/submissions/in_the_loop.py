def do_move(valid_moves, notebook):
    possible_exits = list()
    number_of_turns = 0
    for move in valid_moves:
        new_move = (move['x'], move['y'])

        if new_move not in notebook:

            if move['exit'] == 'yes':
                possible_exits.append((move['x'], move['y']))
                notebook[new_move] = 'exit'
                number_of_turns += 1
                return new_move, notebook
            elif move['type'] == 'normal':
                notebook[new_move] = 'normal'
                number_of_turns += 1
                return do_move(valid_moves, notebook)
            elif move['type'] == 'mud':
                notebook[new_move] = 'mud'
                number_of_turns += 1
                return new_move, notebook

        else: #new_move is in notebook
            if notebook[new_move] == 'exit':
                number_of_turns += 1
                return new_move, notebook

    #print(new_move) 
