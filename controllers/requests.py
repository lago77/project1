from turtle import hideturtle
from flask import jsonify, render_template
from repository.userlogin_dao import *
from repository.requests_dao import *
from models.login_dto import Login
from repository.requests_dao import *
import json
from flask import redirect, url_for, session
from service.valid_amount import *
from service.valid_description import * 
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
    # print(type(request_dict[2]))
    # return request_dict
    print("my request dict")
    print(request_dict)
    return request_dict
    # return render_template('random.html',request=request_dict)

def getrequest(id):

    requests=select_requests_by_id(id)

    # for request in requests:
    request_dict={}
    # request_dict[id]=request
    print("these are the requests")
    # print(request)
    # print("ending loop")
    # print(request_dict)
    # print(type(request_dict[2]))
    # \        self.request_id=request_id
    #     self.user_id = user_id
    #     self.description= description
    #     self.amount = amount
    #     self.status = status

    # request_dict['request_id']=request.request_id
    # request_dict['user_id']=request.user_id
    # request_dict['description']=request.description
    # request_dict['amount']=request.amount
    # request_dict['status']=request.status
    requestdict={}
    for item in requests:
        requestdict[item[0]]=item
    
    print("request dict[id]")
    dict1={1:["Dsfsd"]}
    print(type(dict1[1]))
    print("the new request dictionary")
    print(requestdict)
  
    req_json=jsonify(requestdict)
    # print(request_dict)
    print("req json")
    print(req_json)
    return req_json
    # return render_template('random1.html',request=request_dict, id=id)


def makerequest(description,amount):

    # myupdate = update_request(data['id'],data['status'])
    print("in makerequest")
    print(description)
    print(amount)
    valamount=validate_amount(description)
    valdescription=validate_description(amount)
    # if (valamount and valdescription):
    user=select_user_by_username(session['username'])
    print("my id is")
    id=user.user_id
    print(id)


    requestid=insert_request(id,description,amount)
    # print(requestid)
        
    if session['role']=="Employee":

        return redirect(url_for('dashboardE',user=session['username']))

    else:
        return redirect(url_for('dashboardM',user=session['username']))

    # else:
    #     if session['role']=="Employee":

    #         return redirect(url_for('dashboardE',user=session['username']))

    #     else:
    #         return redirect(url_for('dashboardM',user=session['username']))



def updaterequest(id,status):

    # # myupdate = update_request(data['id'],data['status'])
    # print("my data")
    # print(type(data))
    
    # print(data)
    # # mydata=str(data)
    # mydata = json.loads(data)
    # print(mydata['id'])
    # print(mydata['status'])
    # print(mydata)
    newdata=update_request(id,status)
    # print("new data")
    # print(newdata)
    print("in update request")
    print(id)
    print(status)
    if session['role']=="Employee":

        return redirect(url_for('dashboardE',user=session['username']))

    else:
        return redirect(url_for('dashboardM',user=session['username']))



def deleterequest(id):

    # myupdate = update_request(data['id'],data['status'])
    # print("my data")
    # print(type(data))
    
    # print(data)
    # # mydata=str(data)
    # mydata = json.loads(data)
    # print(mydata['request_id'])
    # print(mydata)
    newdata=delete_requests_by_id(id)
    # print(session['username'])
    # print("new data")
    print("new data is")
    print(newdata)
    print("deleted")
    
    if session['role']=="Employee":

        return redirect(url_for('dashboardE',user=session['username']))

    else:
        return redirect(url_for('dashboardM',user=session['username']))