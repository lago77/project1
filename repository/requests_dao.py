import psycopg2
from repository.connection import get_connection

from models.login_dto import Login
from models.requests_dto import Requests


def select_requests():
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM project1.requests;"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchall()
            if record is None:
                break
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def select_requests_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM project1.requests WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchall()[0]
            if record is None:
                break
            # user_transaction= Transactions(record[0], record[1], record[2], record[3], record[4])

        #             self.request_id=request_id
        # self.user_id = user_id
        # self.description= description
        # self.amount = amount
        # self.status = status
            print("the records")
            print(record)
            print(record[0])
            print("end")
            Request = Requests(record[0], record[1], record[2], record[3], record[4])
            return Request
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def insert_request(userid, description, amount):
    connection = get_connection()
    cursor = connection.cursor()

    print(userid)
    print(type(userid))
    qry = "INSERT INTO project1.requests VALUES (default,%s, %s, %s, %s) RETURNING request_id;"

    try:
        cursor.execute(qry, (userid, description, amount, "Pending"))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def update_request(request_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    qry = "UPDATE project1.requests SET status=%s WHERE request_id = %s RETURNING status;"

    try:
        cursor.execute(qry, (status,request_id))
        status = cursor.fetchone()[0]
        connection.commit()
        print("my id is",str(id))
        print("new status is", status)
        return status
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def delete_requests_by_id(request_id):
    connection = get_connection()
    cursor = connection.cursor()
    print(type(request_id))
    qry = "DELETE FROM project1.requests WHERE request_id = %s;"

    print("query")
    print(qry)
    print(request_id)
    try:
        print("////////executing query")
        cursor.execute(qry,(request_id,))
        print("////query executed")
        connection.commit()
        return "deleted"
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()