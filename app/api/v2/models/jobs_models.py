from app.database.database import Database
from datetime import datetime,timedelta
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