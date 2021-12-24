# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to solve the maze.
def do_move(valid_moves, notebook):
    notebook['old_positions'] = []
    
    surrounding_tiles = []
    
    for moves in valid_moves:
        coordinate = (valid_moves['x'], valid_moves['y'])
        surrounding_tiles.append(coordinate)
        
    if len(surrounding_tiles) == 3:
        if surrounding_tiles[0][0] == surrounding_tiles[1][0]:
            position_x = surrounding_tiles[0][0]
            position_y = (surrounding_tiles[0][1] + surrounding_tiles[1][1]) / 2
            
        if surrounding_tiles[0][0] == surrounding_tiles [2][0]:
            position_x = surrounding_tiles[0][0]
            position_y = (surrounding_tiles[0][1] + surrounding_tiles[2][1]) / 2
            
        if surrounding_tiles[1][0] == surrounding_tiles[2][0]:
            position_x = surrounding_tiles[1][0]
            position_y = (surrounding_tiles[1][1] + surrounding_tiles[2][1]) / 2     
        
        if surrounding_tiles[0][1] == surrounding_tiles[1][1]:
            position_x = (surrounding_tiles[0][0] + surrounding_tiles[1][0]) / 2
            position_y = surrounding_tiles[0][1]
            
        if surrounding_tiles[0][1] == surrounding_tiles[2][1]:
            position_x = (surrounding_tiles[0][0] + surrounding_tiles[1][0]) / 2
            position_y = surrounding_tiles[0][1]
            
        if surrounding_tiles[1][1] == surrounding_tiles[2][1]:
            position_x = (surrounding_tiles[0][0] + surrounding_tiles[1][0]) / 2
            position_y = surrounding_tiles[0][1]  
        
        old_position = (position_x, position_y)
        
        notebook['old_positions'].append(old_position)
        
    if len(surrounding_tiles) == 2:
        old_position_x = (surrounding_tiles[0][0] * surrounding_tiles[1][0]) / 2
        old_position_y = (surrounding_tiles[0][1] * surrounding_tiles[1][1]) / 2
        
        old_position = (old_position_x, old_position_y)

        notebook['old_positions'].append(old_position)
        
        
    for moves in valid_moves:
        
        if valid_moves['exit'] == 'yes':
            new_x = valid_moves['x']
            new_y = valid_moves['y']
        
            new_position = (new_x, new_y)
            notebook['old_position'].append(new_position)
            
        elif valid_moves['type'] == 'normal' and (valid_moves['x'], valid_moves['y']) not in notebook['old_position']:
            new_x = valid_moves['x']
            new_y = valid_moves['y']
            
            new_position = (new_x, new_y) 
            notebook['old_position'].append(new_position)
            
            new_move_x = abs(new_position[0] - old_position[0])
            new_move_y = abs(new_position[1] - old_position[1])
            
            new_move = (new_move_x, new_move_y)
            return new_move
        
        elif valid_moves['type'] == 'mud' and (valid_moves['x'], valid_moves['y']) not in notebook['old_position']:
            new_x = valid_moves['x']
            new_y = valid_moves['y']
            
            new_position = (new_x, new_y) 
            notebook['old_position'].append(new_position)
            
            new_move_x = abs(new_position[0] - old_position[0])
            new_move_y = abs(new_position[1] - old_position[1])
            
            new_move = (new_move_x, new_move_y)
            return new_move
        
        elif valid_moves['type'] == 'normal':
            new_x = valid_moves['x']
            new_y = valid_moves['y']
            
            new_position = (new_x, new_y) 
            notebook['old_position'].append(new_position)
            
            new_move_x = abs(new_position[0] - old_position[0])
            new_move_y = abs(new_position[1] - old_position[1])
            
            new_move = (new_move_x, new_move_y)
            return new_move
        
        elif valid_moves['type'] == 'mud':
            new_x = valid_moves['x']
            new_y = valid_moves['y']
            
            new_position = (new_x, new_y) 
            notebook['old_position'].append(new_position)
            
            new_move_x = abs(new_position[0] - old_position[0])
            new_move_y = abs(new_position[1] - old_position[1])
            
            new_move = (new_move_x, new_move_y)
            return new_move
            
            
            
    new_move_x = abs(new_position[0] - old_position[0])
    new_move_y = abs(new_position[1] - old_position[1])
            
    new_move = (new_move_x, new_move_y)
        
            
    return new_move, notebook

