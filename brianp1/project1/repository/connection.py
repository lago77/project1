import psycopg2

# This file is used to define a function to get the database connection

def get_connection():
    connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="revature123",
            host="project-1.couvk3nfrojy.us-east-1.rds.amazonaws.com",
            port="5432"
    )

    return connection