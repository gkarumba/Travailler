import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime, timedelta
from instance.config import config_by_name

environment = os.getenv('FLASK_ENV')
database_url = "postgres://takxlevmflfwup:2ea8cc1c7a18bace0d7880325242649ff070edd7315f2fbd43dc25f29e01e873@ec2-54-227-246-152.compute-1.amazonaws.com:5432/d5tpoag5lng45u"

class Database():
    """Class with methods to handle the database"""
    def __init__(self):
        """Method for initialising the class"""
        self.conn = psycopg2.connect(database_url)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_tables(self):
        """Method for creating tables"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS jobs_entity(
            job_id SERIAL PRIMARY KEY,
            location varchar(420) NOT NULL,
            title varchar(420) NOT NULL,
            company  varchar(420) NOT NULL,
            responsibility  varchar(420) NOT NULL,
            category varchar(420) NOT NULL,
            salary int NOT NULL,
            deadline varchar(420),
            date_posted varchar(420)
        );""",
        """ CREATE TABLE IF NOT EXISTS user_entity(
            user_id SERIAL PRIMARY KEY,
            username varchar(420) NOT NULL,
            email varchar(420) NOT NULL,
            occupation varchar(420) NOT NULL,
            location varchar(420) NOT NULL,
            age int NOT NULL,
            admin varchar(420) default False,
            education varchar(420) NOT NULL,
            password varchar(420) NOT NULL,
            nationalID int
        );""")

    def create_application_table(self):
        """Method to create the application tables"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS application_entity(
            application_ id SERIAL PRIMARY KEY,
            user_id 
            job_id 
            status varchar(420) NOT NULL
        );""")
    
    def add_job(self,query_data,tuple_data):
        """Method to add job"""
        self.cur.execute(query_data,tuple_data)
        self.conn.commit()

    def add_user(self,query_data,tuple_data):
        """Method to add a user"""
        self.cur.execute(query_data,tuple_data)
        self.conn.commit()

    def get_all_jobs(self,query_data):
        """Method to retrieve all jobs"""
        self.cur.execute(query_data)
        return self.cur.fetchall()

    def get_one_job(self,query_data):
        """Method to retrieve jobs by category"""
        self.cur.execute(query_data)
        return self.cur.fetchone()
    
    def get_one_user(self,query_data):
        """Method to retrieve user"""
        self.cur.execute(query_data)
        return self.cur.fetchone()

    def edit_job(self,query_data):
        """Method to edit a job data"""
        self.cur.execute(query_data)
        self.conn.commit()

    def approve_job(self,query_data):
        """Method to approve a job application"""
        self.cur.execute(query_data)
        self.conn.commit()

    def cancel_job(self,query_data):
        """Method to a cancel a job application"""
        self.cur.execute(query_data)
        self.conn.commit()

    def apply_job(self,query_data,tuple_data):
        """Method to apply for a job"""
        self.cur.execute(query_data,tuple_data)
        self.conn.commit()
        
    def delete_job(self,query_data):
        """Method to remove a job"""
        self.cur.execute(query_data)
        self.conn.commit()
    
    def drop_table(self, table_name):
        drop = f"DROP TABLE {table_name};"
        self.cursor.execute(drop)

         # added_on varchar(420) default current_timestamp,
            # deadline_on varchar(420) 