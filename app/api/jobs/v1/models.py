from flask import abort
from datetime import datetime,timedelta

jobs = []

class JobsModel:
    """
    Class with methods to add a job
    """
    def __init__(self,title,category,responsibility,\
                 company,location,salary):
        self.title = title
        self.category = category
        self.responsibility = responsibility
        self.company = company
        self.location = location
        self.salary = salary
        self.jobId = len(jobs)+1
        self.dateposted = datetime.now()
        self.deadline =  datetime.now() + timedelta(days=21)

    def serialize(self):
        """
        Method to take json data and return a python dictionary
        """
        return {
        "title":self.title,
        "category":self.category,
        "responsibility":self.responsibility,
        "company":self.company,
        "location":self.location,
        "salary":self.salary,
        "jobId":self.jobId,
        "dateposted":self.dateposted,
        "deadline":self.deadline
        }
    def check_job_title(self,titled):
        """
        Method for checking if job title already exists
        """
        for job in jobs:
            if job.title == titled:
                return True
            return False 