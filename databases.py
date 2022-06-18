import re
import psycopg2
from repository.connection import get_connection
from models.login_dto import Login
# DAO = Data Access Object
# For database interaction

from repository.requests_dao import *
def select_users():
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM project1.userLogin;"

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

def select_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM project1.userLogin WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            User = Login(record[0], record[1], record[2])
            return User
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_user_by_username(username):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM project1.userLogin WHERE username = '{username}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                return None
            else:
                User = Login(record[0], record[1], record[2])
                return User
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO project1.userLogin VALUES (default, %s, %s) RETURNING user_id;"


    try:
        cursor.execute(qry, (username, password))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print("the error is")
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


def delete_user_by_username(username,password):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    qry = "DELETE FROM project1.userlogin WHERE username = %s AND password = %s;"

    try:
        cursor.execute(qry, (username,password))
        # id = cursor.fetchone()[0]
        connection.commit()
        message = "Deleted"
        return message
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def delete_user_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    
    qry = "DELETE FROM project1.userlogin WHERE user_id=%s;"

    try:
        cursor.execute(qry,(id,))
        # id = cursor.fetchone()[0]
        connection.commit()
        message = "Deleted"
        return message
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def update_password(user_id, newpass):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    qry = "UPDATE project1.userLogin SET password=%s WHERE user_id = %s RETURNING user_id;"

    try:
        cursor.execute(qry, (newpass,user_id))
        id = cursor.fetchone()[0]
        connection.commit()
        print("my id is",str(id))
        print("new password is", newpass)
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()
# print("type is")
# myuser=select_user_by_id(1)
# print(type(select_user_by_id(1)))
# if (type(select_user_by_id(1))== type(Login)):
#     print("this is a class")

# print(isinstance(myuser,Login))
# print(type(1))

# delval=delete_user_by_id(2)
# print(type(delval))
# print(delval)

# id=insert_request(1, "sfdas3dfsadfsd faf asdfsdfsfsd3fsdf",100)
# print(id)

# id=select_user_by_id(1)
# print(id)

# users=select_users()
# print(users[0][0])
# print(type(users[0]))

# for user in users:
#     print(f"user id ")

requests=tuple(select_requests())
print(type(requests))
print(requests)
# newrequests=tuple(requests)

# print(type(newrequests))
# print(newrequests)