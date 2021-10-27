
# 1st Exercise
# ------------

# (1.a) -------------
def is_friend_of_harry(p_name):
    friends_list = ["Ron", "Hermione", "Hagrid", "Dumbledore"]
    return p_name in friends_list
    # instead of using this:
    # if p_name in friends_list:
    #    return True
    # else:
    #    return False


print(is_friend_of_harry("Hagrid"))
print(is_friend_of_harry("Voldemort"))
print(is_friend_of_harry("Bellatrix"))

# (1.b) -------------
a = is_friend_of_harry("Hagrid")
b = is_friend_of_harry("Voldemort")
c = is_friend_of_harry("Bellatrix")
if a or b or c:
    print("Harry has friends!")
else:
    print("Harry has no friends!!")


# (1.c) -------------
def is_friend_of_harry(p_name):
    friends_list = ["Ron", "Hermione", "Hagrid", "Dumbledore"]
    # transorm the given value in a format similar to the one used for the values of the list
    p_name = p_name.lower()  # e.g. "  HagRId" -> "  hagrid"
    p_name = p_name.strip()  # e.g. "  hagrid" -> "hagrid"
    p_name = p_name.capitalize()  # e.g. "hagrid" -> "Hagrid"
    # Now do the check and return True/False
    return p_name in friends_list


# (1.d) -------------
def is_prof_friend_of_harry(p_name):
    prof_list = ["Snape", "Lupin", "Hagrid", "Dumbledore"]
    p_name = p_name.lower()
    p_name = p_name.strip()
    p_name = p_name.capitalize()
    # check if p_name is in the list of profs and is a friend of Harry
    return p_name in prof_list and is_friend_of_harry(p_name)


print(is_prof_friend_of_harry("  hagrid"))
print(is_prof_friend_of_harry("voldemort"))
print(is_prof_friend_of_harry(" Bellatrix  "))
