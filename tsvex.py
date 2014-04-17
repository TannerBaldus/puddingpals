import csv
filein = open('bad.tsv')
reader = csv.DictReader(filein,delimiter='\t')
row = reader.next()
print row.keys()
