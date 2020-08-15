import uuid      #This module provides a unique id

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() 
    
    def to_dict(self):
        return vars(self)  # bring a dictionary from our objetc

    @staticmethod   #Convert a function in static method which are those who can execute without an isntance of a class
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
    