import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.database.database import Database

db = Database()

class UserModel():
    """Class with the methods to manipulate the database"""
    def add_user(self,email,password,username,occupation,age,\
                 location,education,nationalID):
        """Method of adding a user"""
        Admin = 'True'
        hash_password = generate_password_hash(password)
        # db.create_tables()
        # db.create_tables()
        query = """INSERT INTO user_entity(email,password,username,occupation,age,\
                 location,education,nationalID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
        tuple_data = (email,hash_password,username,occupation,age,\
                      location,education,nationalID)
        db.add_user(query,tuple_data)
        query2 = """SELECT user_id FROM user_entity WHERE user_id = (select max(user_id) from user_entity);"""
        result = db.get_one_user(query2)
        return result

    def check_user_exists(self,nationalID):
        """Method to check if user exists"""
        query = f"""SELECT nationalID FROM user_entity WHERE nationalID ={nationalID};"""
        result = db.get_one_user(query)
        if result:
            return False
        return True
    
    def set_role(self,user_id):
        """
        Method for creating Admin role
        """
        role = 'Admin'
        ID = 12
        query = """SELECT user_id FROM user_entity WHERE user_id = 12;"""
        result  = db.get_one_user(query)
        if result:
            query2 = """UPDATE user_entity SET admin = '{}' WHERE user_id = '{}'""".format(role,ID)
            db.edit_job(query2)
            query3 = """ SELECT * FROM user_entity WHERE user_id = '{}'""".format(ID)
            response = db.get_one_user(query3)
            return response

    def check_user_id(self,user_id):
        """Method to check if a user_id exists"""
        query = f"""SELECT user_id FROM user_entity WHERE user_id ={user_id};"""
        result = db.get_one_user(query)
        if result:
            return True
        return False
    
    def get_user_id(self,nationalID):
        """Method to check if a user_id exists"""
        query = f"""SELECT user_id FROM user_entity WHERE nationalID ={nationalID};"""
        result = db.get_one_user(query)
        # print(result)
        if result:
            return result['user_id']
        return False

    def match_password(self,password,nationalID):
       """Method to match passwords"""
       query = f"""SELECT password FROM user_entity WHERE nationalID = {nationalID};"""
       response = db.get_one_user(query)
    #    print(response)
       result  = check_password_hash(response['password'],password)
       if result:
           return True
       return False
           