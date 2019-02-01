from flask import abort

users = []

class UserModels:
    """
    Class that has the method to register a new user
    """
    def __init__(self,username,age,email,location,\
                 occupation,education,NationalID):
        """
        Method to instatiate the class
        """
        self.username = username
        self.age = age
        self.location = location
        self.occupation = occupation
        self.education = education
        self.NationalID = NationalID
        self.email = email

    def check_id_number(self,id):
        """
        Method for checking if NationalID already exists
        """
        for user in users:
            if user.NationalID == id:
                return True
            return False 

    def serialize(self):
        """
        Method to take json data and return a python dictionary
        """
        return {
            "username":self.username, 
            "age":self.age, 
            "location":self.location, 
            "occupation":self.occupation, 
            "education":self.education, 
            "NationalID":self.NationalID, 
            "email":self.email 
        }
       