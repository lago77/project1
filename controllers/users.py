from repository.userlogin_dao import *
from repository.requests_dao import *
from models.login_dto import Login
from repository.requests_dao import *
from flask import Response
from flask import jsonify
def getusers():

    users=select_users()
    user_dict={}
    for user in users:
        user_dict[user[0]]=user

    print(user_dict)
    print("my response")
    print("my json dict")
    req_json=jsonify(user_dict)
    print(req_json)
    return req_json
    # return user_dict

def getuser(id):

    request=select_user_by_id(id)
    print("my id")
    print(id)
    # for request in requests:
    request_dict={}
    # request_dict[id]=request
    print("my request")
    print(request_dict)
    request_dict['userid']=request.user_id
    request_dict['username']=request.username
    request_dict['password']=request.password
    
    print(request)
    # print("ending loop")
    # print(request_dict)
    # print(type(request_dict[2]))
    print(request)
    print("request dict")
    print(request_dict)


    return request_dict
    # return render_template('random1.html',request=request_dict, id=id)
