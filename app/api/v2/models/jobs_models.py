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
        query = f"""SELECT * FROM jobs_entity WHERE title='{title}';"""
        result = db.get_one_job(query)
        # print(result)
        if result:
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
                
    def edit_job_details(self,cat_id,location,title,company,responsibility,\
                         category,salary):
        """Method to edit a job details"""
        query = f"""SELECT * FROM jobs_entity WHERE job_id = '{cat_id}';"""
        response = db.get_one_job(query)
        if not response:
            return False
        query2 = f"""UPDATE jobs_entity SET title='{title}',location='{location}',company='{company}',\
                    responsibility='{responsibility}',category='{category}',salary='{salary}' WHERE job_id = '{cat_id}';"""
        db.edit_job(query2)
        get_query = f"""SELECT * FROM jobs_entity WHERE job_id='{cat_id}';"""
        response = db.get_one_job(get_query)
        if response:
            return response
        return False

    def serialize(self):
        """Method to take json data and return a python dictionary"""
        return  {
            'location' : self.new_location,
            'title' : self.new_title,
            'company' : self.new_company,
            'responsibility' : self.new_responsibility,
            'category' : self.new_category,
            'salary': self.new_salary
        }
    
    def get_job_by_id(self,job_id):
        """Method to get one job by id"""
        query = f"""SELECT * FROM jobs_entity WHERE job_id='{job_id}';"""
        result = db.get_one_job(query)
        if result:
            keys = ['job_id', 'date_posted','deadline']
            response = [result.pop(key) for key in keys]
            print(result)
            return result
        return False

    def delete_jobs(self,job_id):
        """Method to remove a job"""
        check_query = f"""SELECT * FROM jobs_entity WHERE job_id = '{job_id}';"""
        check_response = db.get_one_job(check_query)
        if not check_response:
            return False
        query = f"""DELETE FROM jobs_entity where job_id = '{job_id}';"""
        db.delete_job(query)