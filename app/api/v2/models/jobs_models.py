from app.database.database import Database
from datetime import datetime,timedelta
from flask import abort,session,make_response,jsonify
db = Database()


class JobModels():
    """Class with method to manipulate the database"""
    def add_job(self,location,title,company,responsibility,\
                category,salary):
        """Method of adding a jobs"""  
        deadline = datetime.now() + timedelta(days=14)
        date_posted = datetime.now()
        query = """INSERT INTO jobs_entity(location,title,company,deadline,date_posted,responsibility,\
                                            category,salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
        tuple_data = (location,title,company,deadline,date_posted,responsibility,category,salary)
        db.add_job(query,tuple_data)
        query2 = """SELECT job_id FROM jobs_entity WHERE job_id = (select max(job_id) from jobs_entity);"""
        result = db.get_one_job(query2)
        return result

    def check_job_exists(self,title):
        """Method for checking if job exists"""
        query = f"""SELECT title FROM jobs_entity;"""
        result = db.get_one_job(query)
        if result['title'] == title:
            return False
        return True

    def get_all_jobs(self):
        """Method to retrieve all jobs"""
        query = """SELECT * FROM jobs_entity;"""
        result = db.get_all_jobs(query)
        if result:
            return result
        return False

    def get_one(self,cat_id):
        """
        Method to retrieve one job
        """
        if cat_id > 6:
            return abort(make_response(jsonify({'message':'Invalid category'}),400))
        categories = {
            2 : "Engineering" ,
            1 : "Medicine" ,
            3 : "Theology"  ,
            4 : "Business"  ,
            5 : "Hospitality"  ,
            6 : "Computer science" 
        }
        for key,value in categories.items():
            # print(key,value)
            if key == cat_id:
                # print(key,value)
                query = f"""SELECT * FROM jobs_entity WHERE category='{value}';"""
                result = db.get_all_jobs(query)
                # print(result)
                if result:
                    return result
                return False
                
        