from AddressBook import AddressBook
from Contact import Contact
import unittest
class ABTest(unittest.TestCase):

	def testAdd(self):
		ab = AddressBook()
		attrs = {'name':'Tester Mcgee','phone':'985.555.555','address':'555 foo lane','zipcode':'70471'}
		ab.addContact(**attrs)
		self.assertEqual(ab.contacts[0].getAttr('name'),'Tester Mcgee')


		
	def testSortName(self):
		names = ['Bane A','Adam C', 'Charles C']
		ab = AddressBook()
		self.fillAb(ab)
		ab.sort('name',False)
		abNames = [contact.getAttr('name') for contact in ab.contacts]
		self.assertEqual(names,abNames)


	def testSortZip(self):
		zips = ['1']



	def testRemove(self):
		ab = AddressBook()
		self.fillAb(ab) ## Adam Charles Bane
		names = ['Charles C','Bane A']
		selected = [0]
		ab.removeSelected(selected)
		abNames = [contact.getAttr('name') for contact in ab.contacts]
		self.assertEqual(names,abNames)


	def testLoadTSV(self):
		ab = AddressBook()
		filein = 'testTSV/tester.tsv'
		ab.loadTSV(filein)
		self.assertEqual(ab.contacts[0].getAttr('name'), 'Dean Baldus')
		self.assertEqual(ab.contacts[1].getAttr('name'),'Tanner Baldus')


	def testWriteTSV(self):
		ab = AddressBook()
		self.fillAb(ab)
		ab.writeTSV('testTSV/testero.tsv')
		ab2 = AddressBook()
		ab2.loadTSV('testTSV/testero.tsv')
		abNames = [contact.getAttr('name') for contact in ab.contacts]
		ab2Names = [contact.getAttr('name') for contact in ab2.contacts]
		self.assertEqual(abNames,ab2Names)

	def testReadTSV(self):
		ab = AddressBook() 
		ab.loadTSV('testTSV/twoWord.tsv')
		c1 = {'name':'Texas Dan', 'phone':'555.377.9285','address':'551 W 13th', 'zipcode':'60155'}
		abContact = ab.contacts[0]
		for key in c1:
			self.assertEqual(abContact.getAttr(key),c1[key])


	def testGoodLabel(self):
		ab = AddressBook()
		c1 = {'name':'Texas Dan', 'phone':'555.377.9285','address':'551 W 13th', 'zipcode':'60155', 'state':'TX',
		'city':'San Antonio','address2':''}
		ab.addContact(**c1)
		label = "Texas Dan\n551 W 13th\nSan Antonio, TX 60155"
		self.assertEqual(ab.contacts[0].getLabel(),label)






	def fillAb(self, ab):
		names = ['Adam C','Bane A','Charles C']
		c1 = {'name':names[0],'phone':'555555555','address':'321 lane', 'zipcode':'97401'}
		c2 = {'name':names[2],'phone':'555444333','address':'123 lane' }
		c3 = {'name':names[1],'phone':'555444222','address':'456 lane'}
		ab.addContact(**c1)
		ab.addContact(**c2)
		ab.addContact(**c3)
		return [c1,c2,c3]


if __name__ == '__main__':
	# ab = AddressBook()
	# ab.loadTSV('testTSV/twoWord.tsv')
	unittest.main()

