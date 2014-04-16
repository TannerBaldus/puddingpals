import csv
import unittest
from Contact import Contact

class AddressBook(object):
	def __init__(self):
		self.contacts = []  ##holds contact objects
		self.changed = False
		self.sortMethod=('name',False)

	def sort(self,attr,isDescending=False):
		contactAttr = lambda contact: contact.getAttr(attr)

		if attr=='name':
			contactAttr = lambda contact: contact.getAttr('name').split(' ')

		self.contacts.sort(key=contactAttr,reverse=isDescending)


	def addContact(self,name='',phone='',address='',zipcode=''):
		""" adds new contact instance to contact list """
		self.contacts.append(Contact(name, phone, address, zipcode))

	def removeSelected(self,selected):
		"""remove contact list from self.contacts """
		for index in selected:
			del self.contacts[index]


	def setTSVfile(self,filepath):
		self.tsvfile = filepath


	def loadTSV(self, filepath):
		tsv = open(filepath,'r')
		reader = csv.DictReader(tsv,delimiter='\t',restval='')
		for row in reader:
			contact = Contact(row['name'],row['phone'], row['address'], row['zipcode'])
			self.contacts.append(contact)


	def writeTSV(self, filepath):
		tsv = open(filepath,'w')
		fieldnames = ['name','phone','address','zipcode']
		writer = csv.DictWriter(tsv, delimiter='\t', fieldnames=fieldnames)
		writer.writerow(dict((fn,fn) for fn in fieldnames))
		for contact in self.contacts:
			writer.writerow(contact.attrs)