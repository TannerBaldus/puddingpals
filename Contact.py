
class Contact(object):

    def __init__(self,**attributes):
        self.attrs = attributes
        self.labelFields = ['address','name','zipcode','city','state']


    def getAttr(self,attr):
        """We can use this to sort the contacts by attribute """
        if attr in self.attrs:
            return self.attrs[attr]
        return ''

    def setName(self,name):
        self.name = name
        self.attrs['name'] = name

    def setPhone(self,phone):
        self.phone = phone
        self.attrs['phone'] = phone

    def setZip(self,zipcode):
        self.zipcode = zipcode
        self.attrs['zipcode'] = zipcode

    def setAddress(self,address):
        self.address = address
        self.attrs['address']=address

    def setAddress2(self,address2):
        self.address2 = address2
        self.attrs['address2'] = address2

    def setCity(self,city):
        self.city = city
        self.attrs['city']=city

    def setState(self,state):
        self.state = state
        self.attrs['state'] = state

    def getLabel(self): 
        if all(self.getAttr(field) for field in self.labelFields):
            mail = ""
            mail += "{}\n".format(self.getAttr('name'))
            mail += "{}\n".format(self.getAttr('address'))
            if self.getAttr('address2') != "":
                mail += "{}\n".format(self.getAttr('address2'))
            mail += "{}, {} {}".format(self.getAttr('city'),self.getAttr('state'),self.getAttr('zipcode'))
        else:
            mail = "Insufficient info to produce mailing label.\nPlease edit contact and try again."

        return mail

