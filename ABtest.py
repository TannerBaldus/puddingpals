from AddressBook import AddressBook
import unittest
class ABTest(unittest.TestCase):

	def testAdd(self):
		ab = AddressBook()
		ab.addContact('Tester Mcgee','985.555.555','555 foo lane','70471')
		self.assertEqual(ab.contacts[0].name,'Tester Mcgee')


		
	def testSort(self):
		names = ['Adam','Bane','Charles']
		ab = AddressBook()
		self.fillAb(ab)
		ab.sort('name',False)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names,abNames)

	def testRemove(self):
		ab = AddressBook()
		self.fillAb(ab) ## Adam Charles Bane
		names = ['Charles','Bane']
		selected = [0]
		ab.removeSelected(selected)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names,abNames)


	def testLoadTSV(self):
		ab = AddressBook()
		filein = 'tester.tsv'
		ab.loadTSV(filein)
		self.assertEqual(ab.contacts[0].name,'Tanner Baldus')
		self.assertEqual(ab.contacts[1].name, 'Dean Baldus')


	def testWriteTSV(self):
		ab = AddressBook()
		self.fillAb(ab)
		ab.writeTSV('testero.tsv')
		ab2 = AddressBook()
		ab2.loadTSV('testero.tsv')
		abNames = [contact.name for contact in ab.contacts]
		ab2Names = [contact.name for contact in ab2.contacts]
		self.assertEqual(abNames,ab2Names)

	def testBadTSV(self):
		ab = AddressBook()
		self.assertEqual('a','b')

	def fillAb(self, ab):
		names = ['Adam','Bane','Charles']
		ab.addContact(names[0],'555555555','321 lane')
		ab.addContact(names[2],'555444666','553 Dr')
		ab.addContact(names[1], '555333222','675 road')


if __name__ == '__main__':
	ab = AddressBook()
	ab.loadTSV('bad.tsv')
	unittest.main()

