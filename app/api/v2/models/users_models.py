import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.database.database import Database

db = Database()

class UserModel():
    """Class with the methods to manipulate the database"""
    def add_user(self,email,password,username,occupation,age,\
                 location,education,nationalID):
        """Method of adding a user"""
        hash_password = generate_password_hash(password)
        # db.create_tables()
        # db.create_tables()
        query = """INSERT INTO user_entity(email,password,username,occupation,age,\
                 location,education,nationalID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
        tuple_data = (email,hash_password,username,occupation,age,\
                      location,education,nationalID)
        db.add_user(query,tuple_data)
        query2 = """SELECT id FROM user_entity WHERE id = (select max(id) from user_entity);"""
        result = db.get_one(query2)
        return result

    def check_user_exists(self,nationalID):
        """Method to check if user exists"""
        query = f"""SELECT id FROM user_entity WHERE id ={nationalID};"""
        if not query:
            return True
        return False
