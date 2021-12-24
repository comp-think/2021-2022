#group.py
# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to solve the maze.


'''def do_move(valid_moves, notebook): #by means of this function, you will fail
    
    new_move = (-1, -1) #something outside the square (-> it's a wrong move on purpose)
    
    return new_move, notebook
'''

'''
Backtracking approach:
Based on a tree defining the legal moves -> tries to identify possible candidate solutions to the problem incrementally and abandons partial candidates if they don't provide solution
It is a recursive algorithm:
!!! CHECK IF THERE ARE MOVES AVAILABLE
1 - Leaf win case
  new_move = None
  if dict["exit"] == "yes": #leaf win base case
      new_move = (valid_moves[x],valid_moves[y])
      
    One of the adjacent rooms is the exit
      I scroll through the list of dictionaries   for dict in valid_moves:
        for each dict I check "exit" key              if dict["exit"] == "yes"
    I must return all the steps that brought me here -> result = notebook 

NOT LEAF-WIN CASE
2 - Leaf lose case
    We don't have any exit amongst the adjacent nodes

3 - RECURSIVE STEP
There are moves available (already checked)
If I only have one room available, I must go there
If I have more than one room
  I just choose one of the many -> I repeat the instructions


Mud-condition:
  If the adjacent room == normal -> we can move once more
  If the adjacent room == mud -> we must stop

Apply recursively the algorithm for each possible valid move executable according to the current status we are in (see: which are the adjacent rooms) until one of these recursive calls returns a solution
'''

'''def do_move(valid_moves, notebook):
  result = None
  for dict in valid_moves:
    if dict["exit"] == "yes": #leaf win base case
      notebook.append(dict) #We save the dictionary with "exit" == "yes"
      result = notebook #in the notebook we will save the sequence of moves to get here
  #If we are not in leaf win we have two possibilities
    if len(valid_moves) == 1:
      dict = valid_moves[0]
      new_room = (dict[x],dict[y])
      #Save the previous room/move in the notebook 
      notebook.append(new_room) #You save the sequence of rooms to get to the exit
      result = notebook
      #return (new_room,notebook)
  return new_move, notebook'''
  
def do_move(valid_moves,notebook):
  new_move = None
  for dict in valid_moves:
    if dict["exit"] == "yes": #leaf win base case: one of the adjacent rooms is the exit
      new_move = (valid_moves[x],valid_moves[y])
      notebook.append(new_move) #We save the move corresponding to the exit room
    elif len(valid_moves)==1:
      new_move = (valid_moves[x],valid_moves[y])
      notebook.append(new_move)
  else:




     #def take_a_step(valid_moves)
     #while len(valid_moves):
     # new_move = (valid_moves[x],valid_moves[y])
     # notebook.append(new_move)  
     
    #for c in valid_moves:         #decrease the len  of valid moves by 1 i.e. pop put a valid move and go to the next move
                                  #if the next move is = exit, then return notebook
  