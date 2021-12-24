import random
import copy


def do_move(valid_moves, notebook):

    if 'history' not in notebook:
        notebook['history'] = []

    best_moves = copy.deepcopy(valid_moves)
    found_exit = False

    for move in best_moves:
        if move['exit'] == 'true':
            found_exit = True
            for temp in best_moves:
                if temp is not move:
                    best_moves.remove(temp)
        break

    if not found_exit:
        dead_end = True
        for move in best_moves:
            if (move['x'], move['y']) not in notebook['history']:
                dead_end = False
                break

    if not dead_end:
        for move in best_moves:
            if (move['x'], move['y']) in notebook['history']:
                best_moves.remove(move)


    swamp = True
    for move in best_moves:
        if move['type'] == 'normal':
            swamp = False
            break

    if not swamp:
        for move in best_moves:
            if move['type'] == 'mud':
                best_moves.remove(move)

    random_move = random.choice(best_moves)
    x = random_move['x']
    y = random_move['y']
    next_move = (x, y)

    notebook['history'].append(next_move)
    return next_move, notebook