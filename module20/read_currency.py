import csv

with open('./data/currencyrates.csv','r') as file:
    lines = csv.reader(file)
    header = next(lines)
    tk = ''
    for line in lines:
        if 'Bangladesh' in line[0]:
            tk = line[3]
            break

    print( float(tk)*50 )


