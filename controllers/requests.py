from turtle import hideturtle
from flask import jsonify, render_template
from repository.userlogin_dao import *
from repository.requests_dao import *
from models.login_dto import Login
from repository.requests_dao import *
import json

def getrequests():

    requests=tuple(select_requests())
    
    print("my requests")
    request_dict={}
    # for x in requests:
    #     print(x)
    mydict={"value":"this is new", "value2":["testing list","another item"]}
    for request in requests:
        request_dict[request[0]]=request
    
    print("ending loop")
    print(request_dict)
    print(type(request_dict[2]))
    # return request_dict
    print("my request dict")
    print(request_dict)
    return request_dict
    # return render_template('random.html',request=request_dict)

def getrequest(id):

    request=select_requests_by_id(id)

    # for request in requests:
    request_dict={}
    # request_dict[id]=request
    print(request)
    # print("ending loop")
    # print(request_dict)
    # print(type(request_dict[2]))
    # \        self.request_id=request_id
    #     self.user_id = user_id
    #     self.description= description
    #     self.amount = amount
    #     self.status = status

    request_dict['request_id']=request.request_id
    request_dict['user_id']=request.user_id
    request_dict['description']=request.description
    request_dict['amount']=request.amount
    request_dict['status']=request.status
    print(request)
    print("request dict[id]")
    print(request_dict)
    return "hei"
    # return render_template('random1.html',request=request_dict, id=id)


def makerequest(data):

    # myupdate = update_request(data['id'],data['status'])
    print("data")
    print(data)
    # print("my data")
    # print(type(data))
    
    # print(data)
    # mydata=str(data)
    # print(mydata)
    mydata = json.loads(data)
    print("mydata")
    print(mydata)
    # print(mydata['id'])
    # print(mydata['status'])
    # print(mydata)
    requestid=insert_request(mydata['userid'],mydata['description'],mydata['amount'])
    print(requestid)
    # print("new data")
    # print(newdata)
    print("ending the function")
    makedict={"requestid":requestid}
    
    return makedict



def updaterequest(data):

    # myupdate = update_request(data['id'],data['status'])
    print("my data")
    print(type(data))
    
    print(data)
    # mydata=str(data)
    mydata = json.loads(data)
    print(mydata['id'])
    print(mydata['status'])
    print(mydata)
    newdata=update_request(mydata['id'],mydata['status'])
    print("new data")
    print(newdata)
    return "in update request"



def deleterequest(data):

    # myupdate = update_request(data['id'],data['status'])
    print("my data")
    print(type(data))
    
    print(data)
    # mydata=str(data)
    mydata = json.loads(data)
    print(mydata['request_id'])
    print(mydata)
    newdata=delete_requests_by_id(mydata['request_id'])
    # print("new data")
    print(newdata)
    print("deleted")
    return newdata