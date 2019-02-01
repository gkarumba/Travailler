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
            if job.title == titled:
                return True
            return False 
    
    def get_all(self):
        """
            Method for retrieving all the books
        """
        return jobs
