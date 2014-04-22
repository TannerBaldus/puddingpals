import unittest
from string import punctuation
from Contact import Contact
from FileHandler import FileHandler

class AddressBook(object):


    def __init__(self):
        self.contacts = []  ##holds contact objects
        self.changed = False
        self.sortMethod=('name',False)
        self.FileHandler = FileHandler()

    def sort(self,attr,isDescending=False):
        contactAttr = lambda contact: contact.getAttr(attr).translate(None,punctuation)

        if attr=='name':

            contactAttr = lambda contact: contact.getAttr(attr).split(' ')[::-1] ##puts last name first in split list

        self.contacts.sort(key=contactAttr,reverse=isDescending)


    def addContact(self,**attrs):
        """ adds new contact instance to contact list """
        contact = Contact(**attrs)
        self.contacts.append(contact)



    def removeSelected(self,selected):
        """remove contact list from self.contacts """
        for index in selected:
            del self.contacts[index]

    def loadTSV(self, filepath):
       fromTSV = self.FileHandler.readUSPS(filepath)
       for attr in fromTSV :
        self.contacts.append(Contact(**attr))

            

    def writeTSV(self, filepath):
        self.FileHandler.writeUSPS(self.contacts,filepath)

