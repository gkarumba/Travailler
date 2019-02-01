import re

# class Validate():
#     """
#     Class with Functions to validate inputs
#     """
def validate_email(email):
    """
    Function to validate an email address
    """
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return False
    return True

def check_space(mystring):
    """
    Function for validating whitespaces/blanks
    """
    if mystring and mystring.strip():
        return True
    else:
        return False

def validate_username(username):
    """
    Function to validate a username
    """
    if not re.match(r"^[A-Za-z0-9\.\+_-]*$", username):
        return False
    return True

def validate_age(age):
    """
    Function to validate a user's age
    """
    if not len(str(age)) == 2:
        return False
    return True

def validate_education(education):
    """
    Function to validate the user's education
    """
    qualification = 'Diploma,Certificate,Degree,Masters,PhD'
    if education in qualification:
        return True
    return False

def validate_location(location):
    """
    Function to validate a user's location
    """
    if not re.match(r"^[A-Za-z0-9\.\+_-]*$", location):
        return False
    return True

def validate_NationalID(NationalID):
    """
    Function to validate the user's NationalID
    """
    if not len(str(NationalID)) == 8:
        return False
    return True

def validate_occupation(occupation):
    """
    Function to validate the user's occupation
    """
    works = ['Employed','Unemployed','Retired']
    for occ in works:
        if occ == occupation:
            return True
        return False
