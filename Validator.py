import csv

class Validator(object):
	def __init__(self):
		pass
	def sanitize(self,string):
		string.replace('\t','    ')

	def isValidPhone(self,rawphone):
		exclude = set(string.punctuation)
		phone = "".join(c for c in rawphone if c not in (exclude))
		if len(phone) in range(7,17): ##limit on len http://goo.gl/8jyLcS


	def isValidTSV(self,filein):
		reader = csv.DictReader(filein)
		fieldnames = ['name','phone','address','zip']
		line = reader[0]
		try
			
