import group
from json import load
from collections import OrderedDict

def load_labirinth(labyrinth_file_path):  # TODO: missing handling of differente cells
    with open(labyrinth_file_path, encoding="utf-8") as f:
        labirinth_json = load(f)

        structure = {}
        for cell in labirinth_json["structure"]:
            structure[(cell["x"], cell["y"])] = cell["type"]

        return (labirinth_json["entrance"]["x"], labirinth_json["entrance"]["y"]), \
               [(exit["x"], exit["y"]) for exit in labirinth_json["exits"]], \
               structure

def get_valid_moves(player_name, position, status, labyrinth, exits):
    result = []

    x = position[0]
    y = position[1]
    
    if (x - 1, y) in labyrinth:
        result.append({
            "x": x - 1,
            "y": y,
            "type": labyrinth[(x - 1, y)],
            "players": get_players_in_cell((x - 1, y), status, player_name),
            "exit": "yes" if (x - 1, y) in exits else "no"
        })
    if (x + 1, y) in labyrinth:
        result.append({
            "x": x + 1,
            "y": y,
            "type": labyrinth[(x + 1, y)],
            "players": get_players_in_cell((x + 1, y), status, player_name),
            "exit": "yes" if (x + 1, y) in exits else "no"
        })
    if (x, y - 1) in labyrinth:
        result.append({
            "x": x,
            "y": y - 1,
            "type": labyrinth[(x, y - 1)],
            "players": get_players_in_cell((x, y - 1), status, player_name),
            "exit": "yes" if (x, y - 1) in exits else "no"
        })
    if (x, y + 1) in labyrinth:
        result.append({
            "x": x,
            "y": y + 1,
            "type": labyrinth[(x, y + 1)],
            "players": get_players_in_cell((x, y + 1), status, player_name),
            "exit": "yes" if (x, y + 1) in exits else "no"
        })

    return result


def get_players_in_cell(position, status, avoid_player):
    result = set()

    for player_name, player_position in status.items():
        if player_name != avoid_player and position == player_position:
            result.add(player_name)
    
    return result


def check_validity(player_name, move, labyrinth, cheaters, status, new_status):
    result = True

    if move not in labyrinth:
        cheaters.add(player_name)
        if player_name in status:
            del status[player_name]
        if player_name in new_status:
            del new_status[player_name]
        result = False

    return result


def is_winner(player_name, move, exits, current_turn, final_result):
    result = False
    
    if move in exits:
        result = True
        winners = final_result.get(current_turn)
        
        if winners is None:
            winners = []
            final_result[current_turn] = winners

        winners.append(player_name)
    
    return result


def play(players, status, notebooks, current_turn,
         exits, labyrinth, final_results, cheaters, winners):

    new_status = {}

    for player in players:
        player_name = player.__name__
        
        if player_name not in cheaters and player_name not in winners:
            valid_moves = get_valid_moves(player_name, status[player_name], 
                                          status, labyrinth, exits)
            
            new_move, updated_notebook = \
                player.do_move(valid_moves, notebooks[player_name])
              
            right_behaviour = check_validity(player_name, new_move, labyrinth, cheaters, status, new_status)
            
            if right_behaviour:
                if is_winner(player_name, new_move, exits, current_turn, final_results):
                    winners.add(player_name)
                elif labyrinth[new_move] == "normal":
                    valid_moves = get_valid_moves(player_name, new_move, 
                                                status, labyrinth, exits)

                    new_move, updated_notebook = \
                        player.do_move(valid_moves, updated_notebook)
                    
                    right_behaviour = check_validity(player_name, new_move, labyrinth, cheaters, status, new_status)
                    
                    if right_behaviour and is_winner(player_name, new_move, exits, current_turn, final_results):
                        winners.add(player_name)

            if right_behaviour:
                notebooks[player_name] = updated_notebook
                new_status[player_name] = new_move

    status.update(new_status)
    return len(cheaters) + len(winners) == len(players)

if __name__ == "__main__":
    all_players = [group]
    cur_entrance, cur_exits, cur_labyrinth = load_labirinth("test_labyrinth.json")
    final_rank = OrderedDict()
    cur_status = {}
    notebooks = {}

    for player in all_players:
        player_name = player.__name__
        cur_status[player_name] = cur_entrance
        notebooks[player_name] = {}
    
    cheaters = set()
    winners = set()
    for current_turn in range(1, 26):
        all_players_out = play(all_players, cur_status, notebooks, current_turn,
                               cur_exits, cur_labyrinth, final_rank, 
                               cheaters, winners)
        if all_players_out:
            break
    
    print("\n## FINAL RANKS ##")
    for rank, info in enumerate(final_rank.items(), 1):
        print("\nRank", rank)
        print(" ,".join(info[1]), "at turn", info[0])
