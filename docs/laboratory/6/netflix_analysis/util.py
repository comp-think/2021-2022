import csv


def csv_to_matrix(f_path):
    result = []
    with open(f_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            result.append(row)
    return result


def csv_to_list_of_dict(f_path):
    result = []
    with open(f_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result


m = csv_to_list_of_dict("netflix_analysis/data/netflix_titles.csv")

print(m[3])
