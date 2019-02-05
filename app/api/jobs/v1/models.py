from flask import abort
from datetime import datetime,timedelta

jobs = []

class JobsModel():
    """
    Class with methods to add a job
    """
    def __init__(self):
        """
            Constructor method for the class BooksModel
        """
        self.db = jobs

    def add_job(self,title,company,category,responsibility,\
                 salary,location):
        """
            Method for serializing the data of a book
        """
        payload = {
            'location' : location,
            'title' : title,
            'company' : company,
            'responsibility' : responsibility,
            'category' : category,
            'salary': salary,
            'jobid' : len(jobs) + 1,
            'added_on'  : datetime.now(),
            'deadline_on' : datetime.now() + timedelta(days=14)
        } 
        check_title = self.check_job_title(title)
        if check_title == True:
            return 'job already exists'
        else:
            self.db.append(payload)
            for pos in self.db:
                return pos
        
    def check_job_title(self,titled):
        """
        Method for checking if job title already exists
        """
        for job in jobs:
            if job['title'] == titled:
                return True
            return False 
    
    def get_all(self):
        """
        Method for retrieving all the books
        """
        return jobs

    def get_one(self,cat_id):
        """
        Method to retrieve one job
        """
        categories = {
            2 : "Engineer" ,
            1 : "Medicine" ,
            3 : "Theology"  ,
            4 : "Business"  ,
            5 : "Hospitality"  ,
            6 : "Computer science" 
        }
        for key,value in categories.items():
            # print(key,value)
            if key == cat_id:
                print(key,value)
                for job in jobs:
                    print(job)
                    print(job['category'])
                    if job['category'] == value:
                        return job
                    # return False
            #     return False
            # return False
    
    def get_job_by_id(self,id):
        """
        Method for checking if a job exists
        """
        for job in jobs:
            if job['jobid'] == id:
                return True
            return False

    def change_job_details(self,title,company,category,\
                            responsibility,salary,location):
        """
        Method to allow change of job details
        """
        # job = self.get_one(id)
        if len(jobs) > 0:
            jobs[0]['title'] = title
            jobs[0]['company'] = company
            jobs[0]['category'] = category
            jobs[0]['responsibility'] = responsibility
            jobs[0]['salary'] = salary
            jobs[0]['location'] = location
            return jobs[0]

        