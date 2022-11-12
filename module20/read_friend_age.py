import csv

with open('./data/my_friends.csv', 'r') as file:
    lines = csv.reader(file)
    header = next(lines)
    # print('Skip the line that\'s why using there heder to hold heading in this value in header variable', header)
    for line in lines:
        print(line)
