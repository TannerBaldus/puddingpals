import csv
import re
from FileHandler import FileHandler
from string import punctuation


class Validator(object):
	def __init__(self):
		fh = FileHandler()
		self.usps =  fh.uspsFields


	def sanitize(self,string):
		exclude = {'\t':'    ','\n':''}
		for ch in exclude:
			string = string.replace(ch,exclude[ch])
		return string

	# def isvalidPunct(self,ch,validPunct):
	# 	"""Helper function that checks if the punctuation is acceptable """
	# 	if ch in punctuation and not in validPunct:
	# 		return False
	# 	return True


	def isUSPhone(self,rawphone):
		phone = ''
		for ch in rawphone:
			if ch.isdigit():
				phone += ch
		if len(phone) in range(7,12): return True
		return False


	def isValidUSPS(self,filein):
		reader = csv.DictReader(filein)
		row = reader.next()
		fields = uspsFields
		return all(field in row.keys for field in fields)

	def isValidZip(self,zip):
		return re.match(r'9([0-2]|3[0-5]).+', zipcode)


	def isValidState(self,state):
		"""
		Returns State Code if a valid full name or Code
		otherwise returns false

		"""
		if state.isalpha():
			return True
		return False 

	def isValidLabel(self,contact):
		if 



if __name__ == '__main__':
	v = Validator()
	x = 'Hello \t Roger \n Rabbit'
	v.sanitize(x)




		
			
