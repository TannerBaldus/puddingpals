import csv
filein = open('testTSV/badformat.tsv')
reader = csv.DictReader(filein,delimiter='\t')
for row in reader:
	print row
