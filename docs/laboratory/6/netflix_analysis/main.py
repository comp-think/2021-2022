from util import *

netflix_data = csv_to_list_of_dict("netflix_analysis/data/netflix_titles.csv")

# a ----
directors_index = dict()
max_val = 0
max_name = None
for row in netflix_data:
    for director in row["director"].split(", "):
        # detect the empty values
        if director == "":
            continue
        # The value is OK, so ...
        if director not in directors_index:
            directors_index[director] = 0
        directors_index[director] += 1

        # check if the new value is higher than max
        new_val = directors_index[director]
        if new_val > max_val:
            max_name, max_val = director, new_val

print(max_name, max_val)


# b ----
country_cat_index = dict()
for row in netflix_data:
    for country in row["country"].split(", "):
        # detect the empty values
        if country == "":
            continue
        # The value is OK, so ...
        if country not in country_cat_index:
            country_cat_index[country] = dict()

        for cat in row["listed_in"].split(", "):
            # detect the empty values
            if cat == "":
                continue
            # The value is OK, so ...
            if cat not in country_cat_index[country]:
                country_cat_index[country][cat] = 0
            country_cat_index[country][cat] += 1


for k, v in country_cat_index.items():
    print(k, v, "\n")
