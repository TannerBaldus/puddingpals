import csv
import unittest
import docopt








class AddressBook(object):

	def __init__(self,csvfile=''):
		self.contacts = []  ##holds contact objects
		# csvfile = open(csvfile,'rb')
		# self.reader=reader(csvfile)


	def sort(self,attr,isDescending):
		contactAttr = lambda contact: contact.getAttr(attr)
		self.contacts.sort(key=contactAttr,reverse=isDescending)

	def addContact(self,name='',phone='',address='',zipcode=''):
		""" adds new contact instance to contact list """
		self.contacts.append(Contact(name, phone, address, zipcode))

	def removeSelected(self,selected):
		"""remove contact list from self.contacts """
		for index in selected:
			del self.contacts[index]

	def setTSVfile(self,filepath):
		self.tsvfile = open()



	def loadTSV(self, filepath):
		tsv = open(filepath,'r')
		reader = csv.DictReader(tsv,delimiter='\t')
		for row in reader:
			contact = Contact(row['name'],row['phone'], row['address'], row['zip'])
			self.contacts.append(contact)


	def writeTSV(self, filepath):
		tsv = open(filepath,'w')
		writerr = csv.DictWriter(tsv,)
		fieldnames = ['name','phone','address','zip']
		writer.writerow(dict((fn,fn) for fn in fieldnames))
		for contact in self.contacts:
			writer.writerow(contact.attrs)




class ABTest(unittest.TestCase):

	def testAdd(self):
		ab = AddressBook()
		ab.addContact('Tester Mcgee','985.555.555','555 foo lane','70471')
		self.assertEqual(ab.contacts[0].name,'Tester Mcgee')


		
	def testSort(self):
		ab = AddressBook()
		names = ['Adam','Bane','Charles']
		ab.addContact(names[2])
		ab.addContact(names[1])
		ab.addContact(names[0])
		ab.sort('name',False)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names,abNames)

	def testRemove(self):
		ab = AddressBook()
		names = ['Adam','Bane','Charles']
		ab.addContact(names[0])
		ab.addContact(names[1])
		ab.addContact(names[2])
		selected = [0]
		ab.removeContact(selected)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names[1:],abNames)


	def testLoadTSV(self):
		ab = AddressBook()
		filein = 'tester.tsv'
		ab.loadTSV(filein)
		self.assertEqual(ab.contacts[0].name,'Tanner Baldus')
		self.assertEqual(ab.contacts[1].name, 'Dean Baldus')


	def testWriteTSV(self):
		ab = AddressBook
		names = ['Adam','Bane','Charles']
		ab.addContact(names[0],'555555555','321 lane')
		ab.addContact(names[1],'555444666','553 Dr')
		ab.addContact(names[2], '555333222','675 road')
		ab2 = AddressBook()
		ab2.loadTSV()






if __name__ == '__main__':
	unittest.main()









		
