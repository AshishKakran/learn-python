#!/usr/bin/python3

class Contact:
    all_contacts = []   #class variable

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # will be updated for all instances of this class


class Supplier(Contact):  #inherit class Contact or class Supplier extends Contact
    def order(self,order):
        print("If this were a real system we would send "
                "{} order to {}".format(order,self.name))

# overriding and Super

class Friend(Contact):
    def __init__(self,name,email,phone):
        super().__Init__(name,email)
        self.phone = phone

        
