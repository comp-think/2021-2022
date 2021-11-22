# 1st Exercise
# ------------

# the function takes a list of pokemons
# the list is compused by N items (i.e., pokemons)
def pokemon_champion(l_table):
    len_list = len(l_table)
    # Base case 1: if the list has only 1 item
    # -> return just that item
    if len_list == 1:
        return [l_table[0]]
    # Base case 2: if the list has 2 items
    # -> match the 2 items and return the winner
    elif len_list == 2:
        # attacking points of the element on the left
        p_attack = l_table[0][1]
        # defending points of the element on the right
        p_defend = l_table[1][2]
        # match the 2 pokemons and return the winner
        if p_attack > p_defend:
            return [l_table[0]]
        else:
            return [l_table[1]]

    # in this case the list is composed by N items
    # divide the list in two parts, and call the function recursevly
    else:
        # the middle position
        mid = len_list // 2
        return pokemon_champion(
            # the first part of the list
            pokemon_champion(l_table[:mid])
            +
            # the second part of the list
            pokemon_champion(l_table[mid:])
        )


# a tournament of 8 pokemons
pokemon_tournament = [
    ("Poliwag", 10, 5), ("Charmander", 15, 2),
    ("Abra", 8, 7), ("Pidgey", 4, 5),
    ("Goldeen", 6, 8), ("Bulbasaur", 12, 10),
    ("Charmeleon", 18, 8), ("Psyduck", 3, 4)]

# Expected result is ->
# ROUND 1:
#   ("Poliwag",10,5)vs("Charmander",15,2) => ("Poliwag",10,5)
#   ("Abra",8,7)vs("Pidgey",4,5) => ("Abra",8,7)
#   ("Goldeen",6,8)vs("Bulbasaur",12,10) => ("Bulbasaur",12,10)
#   ("Charmeleon",18,8)vs("Psyduck",3,4) => ("Charmeleon",18,8)
#
# ROUND 2:
#   ("Poliwag",10,5)vs("Abra",8,7) => ("Poliwag",10,5)
#   ("Bulbasaur",12,10)vs("Charmeleon",18,8) => ("Bulbasaur",12,10)
#
# THE FINAL:
#   ("Poliwag",10,5)vs("Bulbasaur",12,10) => ("Bulbasaur",12,10)
#
# THE WINNER:
#   ("Bulbasaur",12,10)

# Call the function and print the winner
winner = pokemon_champion(pokemon_tournament)
print(winner)
