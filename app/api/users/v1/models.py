from flask import abort
from werkzeug.security import generate_password_hash,check_password_hash
users = []

class UserModels:
    """
    Class that has the method to register a new user
    """
    def __init__(self,username,age,email,location,\
                 occupation,education,NationalID,\
                 password):
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
        self.password = generate_password_hash(password)

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
        
    def validate_password(self,password):
        """
        Method to validate the user password
        """
        for user in users:
            if check_password_hash(user.password,password):
                return True
            return False
    
    def validate_username(self,username):
        """
        Method to validate the username
        """
        for user in users:
            if user.username == username:
                return True
            return False


