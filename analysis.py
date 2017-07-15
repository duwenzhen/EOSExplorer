import csv
import operator

dict = {}
with open('replace2', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        if not dict.__contains__(row[3]):
            dict[row[3]] = float(row[4])
        else:
            dict[row[3]] = dict[row[3]]  + float(row[4])

sorteddict = sorted(dict.items(), key=operator.itemgetter(1))

for elt in sorteddict[-50:]:
    print(elt)