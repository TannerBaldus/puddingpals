import csv
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


    def setTSVfile(self,filepath):
        self.tsvfile = filepath


    def loadTSV(self, filepath):
        tsv = open(filepath,'r')
        reader = csv.DictReader(tsv,delimiter='\t',restval='')
        for row in reader:
            contact = Contact(**self.FileHandler.readUSPS(row))
            self.contacts.append(contact)


    def writeTSV(self, filepath):
        tsv = open(filepath,'w')
        writer = csv.DictWriter(tsv, delimiter='\t', fieldnames=self.FileHandler.uspsFields)
        writer.writeheader()
        for contact in self.contacts:
            self.FileHandler.writeUSPS(contact,writer)

