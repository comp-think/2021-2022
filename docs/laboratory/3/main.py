# 1st Exercise
# ------------
l_schedule = ["Introduction to the course", "Introduction to Computational Thinking", "Algorithms", "Laboratory", "Computability", "Programming languages", "Organising information: ordered structures", "Laboratory", "Brute-force algorithms", "Laboratory",
              "Organising information: unordered structures", "Laboratory", "Recursion", "Laboratory", "Divide and conquer algorithms", "Laboratory", "Dynamic programming algorithms", "Organising information: trees", "Backtracking algorithms", "Organising information: graphs", "Greedy algorithms"]

# (1.a) -------------


def lab_lessons(a_list):
    count = 0
    for title in a_list:
        if title == "Laboratory":
            count += 1
    return count


print(lab_lessons(l_schedule))


# (1.b) -------------
def all_before_lab(a_list):
    result = []
    i = 0
    title = a_list[i]
    while title != "Laboratory":
        result.append(title)
        i += 1
        title = a_list[i]
    return result


print(all_before_lab(l_schedule))


# (1.c) -------------
l_schedule_extended = [(2, "11/10/21", "09:30-11:30", "Introduction to the course"), (2, "13/10/21", "09:30-11:30", "Introduction to Computational Thinking"), (2, "15/10/21", "12:30-14:30", "Algorithms"), (2, "18/10/21", "09:30-11:30", "Laboratory"), (2, "20/10/21", "09:30-11:30", "Computability"), (2, "22/10/21", "12:30-14:30", "Programming languages"), (2, "25/10/21", "09:30-11:30", "Organising information: ordered structures"), (2, "27/10/21", "09:30-11:30", "Laboratory"), (2, "29/10/21", "12:30-14:30", "Brute-force algorithms"), (2, "08/11/21", "09:30-11:30", "Laboratory"), (2, "10/11/21", "09:30-11:30",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          "Organising information: unordered structures"), (2, "15/11/21", "09:30-11:30", "Laboratory"), (2, "17/11/21", "09:30-11:30", "Recursion"), (2, "22/11/21", "09:30-11:30", "Laboratory"), (2, "24/11/21", "09:30-11:30", "Divide and conquer algorithms"), (2, "29/11/21", "09:30-11:30", "Laboratory"), (2, "01/12/21", "09:30-11:30", "Dynamic programming algorithms"), (2, "06/12/21", "09:30-11:30", "Organising information: trees"), (2, "13/12/21", "09:30-11:30", "Backtracking algorithms"), (2, "15/12/21", "09:30-11:30", "Organising information: graphs"), (2, "20/12/21", "09:30-11:30", "Greedy algorithms")]
# in this new version of l_schedule, each item is a tuple, such that:
# ([HOURS],[DATE],[TIME],[TITLE])


def max_lessons_hours(a_list, max_hours):
    result = []
    tot_hours = 0
    i = 0
    while tot_hours < max_hours:
        title = a_list[i][3]
        result.append(title)
        tot_hours += a_list[i][0]
        i += 1
    return result


print(max_lessons_hours(l_schedule, 10))
