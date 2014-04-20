import csv


class Validator(object):
    def __init__(self):
        pass

    @staticmethod
    def sanitize(self,string):
        string.replace('\t','    ')


    @staticmethod
    def validName(name):
        return True


    @staticmethod
    def validPhone(phone):
        return True

    @staticmethod
    def validAddress(address):
        return True


    @staticmethod
    def validCity(city):
        return True


    @staticmethod
    def validState(state):
        return True


    @staticmethod
    def validZip(zipcode):
        return True


    """def isValidPhone(self,rawphone):
        exclude = set(string.punctuation)
        phone = "".join(c for c in rawphone if c not in (exclude))
        if len(phone) in range(7,17): ##limit on len http://goo.gl/8jyLcS"""


    @staticmethod
    def isValidTSV(self,filein):
        reader = csv.DictReader(filein)
        row = reader.next()
        fields = ['name']
        return all(field in row.keys for field in fields )





