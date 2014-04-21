import csv
import re
import os.path
from string import punctuation


class Validator(object):
	def __init__(self):
		pass

	@staticmethod
	def sanitize(string):
		exclude = {'\t':'    ','\n':''}
		for ch in exclude:
			string = string.replace(ch,exclude[ch])
		return string

	@staticmethod
	def isValidPhone(rawphone):
		phone = rawphone.translate(None,punctuation)
		if len(phone) < 7: return False
		return True

	@staticmethod
	def isValidUSPS(self,filein):
		reader = csv.DictReader(filein)
		row = reader.next()
		return all(field in row for field in self.uspsFields)


	@staticmethod
	def isValidZip(zipcode):
		 if re.match("^\\d{5}(-\\d{4})?$",zipcode): return True
		 return False

	@staticmethod
	def isValidCity(city):
		"""Always Return True for now but might want to expand later"""
		return True




	@staticmethod
	def isValidState(state):
		"""

		"""
		if state.isalpha():
			return True
		return False 

	@staticmethod
	def isValidName(state):
		return True


	@staticmethod
	def isValidUSPS(filein):
		if os.path.isfile(filein) and filein.endswith('.tsv') :
			fields = ['Last','Delivery','Second','Recipient','Phone']
			reader = csv.DictReader(filein)
			row = reader.next()
			return all(field in row.keys for field in fields)
		
		return False




if __name__ == '__main__':
	v = Validator()
	x = 'Hello \t Roger \n Rabbit'
	v.sanitize(x)