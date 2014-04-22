import csv
filein = open('testTSV/twoWord.tsv')
usps = ['Last','Delivery','Second','Recipient','Phone']
reader = csv.DictReader(filein,delimiter='\t')
print all( field in reader.fieldnames for field in usps)
