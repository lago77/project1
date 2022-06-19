from flask import Flask
from flask import render_template
from flask import request
import json
from flask import Flask, redirect, url_for, request, session
from controllers.dashboard import *
from controllers.registration import *
from controllers.requests import *
from controllers.users import *
from flask_cors import CORS, cross_origin 
from flask import Response

app = Flask(__name__)
CORS(app)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/loginpage', methods=['GET'])
def loginpage():
    return render_template('login.html')

@app.route('/registrationpage', methods=['GET'])
def registrationpage():
    return render_template('registration.html')

@app.route('/nextpage')
@app.route('/login',methods = ['POST'])
def login():
   print("the request is in login")
#    print(request.data)
#    mydata=json.loads(request.data)
#    userdata="sdfsd"
   print(request.form)
   print(request.form['username'])
   username=request.form['username']
   password=request.form['password']
   session['username']=username
   user=select_user_by_username(username)
   session['role']=user.role
   session['userid']=user.user_id
   if request.method == 'POST':
      print("in post")
    #   print(mydata)
    #   print(type(mydata))
      userdict={"username":username, "password":password}
      print(userdict)
      print("role")
      print(user.role)
      if user.role=="Employee":
        print("you are an employee")
        return redirect(url_for('dashboardE',user=session['username']))
      else:
        print("you are a manager")
        return redirect(url_for('dashboardM',user=session['username']))

@app.route('/dashboardE', methods=['GET'])
def dashboardE():

    print("in dashboard")
    print(request.args)
    print(request.args['user'])
    print(type(request.args['user']))
  
    # print(type(request.args['userdata']))
    # username=request.args['username']
    # password=request.args['password']
    username="test"
    password="test"
    return my_dashboard(request.args)

@app.route('/dashboardM', methods=['GET'])
def dashboardM():

    print("in dashboard")
    print(request.args)
    print(request.args['user'])
    print(type(request.args['user']))
    # print(type(request.args['userdata']))
    # username=request.args['username']
    # password=request.args['password']
    username="test"
    password="test"
    return my_dashboard(request.args)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('main.html')

@app.route('/requests',methods=['GET'])
def requests():
    return getrequests()

@app.route('/users',methods=['GET'])
@cross_origin()
def users():
    return getusers()

@app.route('/get_user/<id>',methods=['GET'])
def get_user(id):
    print("in get_user")
    return getuser(id)

@app.route('/make_request/',methods=['POST'])
# @cross_origin()
def makereq():
    
    print("my data")
    data="test"
    print("my request")
    id=5
    print("form")
    print(request.form)
    description=request.form['description']
    amount=request.form['amount']
    # print(request.data)
    # Response = flask.jsonify(request.data)
    # Response.headers.add('Access-Control-Allow-Origin', '*')
    # mydict={"value":id, "value2":status}
    return makerequest(description,amount)



@app.route('/update_request/',methods=['POST','GET'])
def updatereq():
    
    print("my data")
    data="test"
    print("my request")
    print(request.form)
    print(request.form['requestid'])
    id=request.form['requestid']
    status="test"
    # print(request.form[0])
    for x in request.form:
        print("printing form")
        print(x)
        if x=="Approve" or x=="Deny":
            status=x
            break
    print(id)
    # mydict={"value":id, "value2":status}
    return updaterequest(id,status)


@app.route('/delete_request/',methods=['POST'])
def deletereq():
    
    print("my data")
    data="test"
    print("my request")
    print(request.form)
    print(request.form['requestid'])
    id=request.form['requestid']
    # mydict={"value":id, "value2":status}
    return deleterequest(id)


@app.route('/get_request/<id>',methods=['GET'])
def get_req(id):
    print("in getreq")
   
    return getrequest(id)


# @app.route('/get_request_user/<id>',methods=['GET'])
# def get_req_user(id):
#     print("in getreq")
   
#     return getrequestuser(id)



@app.route('/register',methods = ['POST'])
def register():


    # username = request.form['username']
    # password = request.form['password']
    print("my request")
    print("round two")
    print(request.form)

    username=request.form['username']
   
    password=request.form['password']
    role=request.form['role']
    id=insert_user(username, password, role)
    print("request.form")
    print(request.form)
    Fruit_Dict = {
    'name': 'Apple',
    'color': 'Red',
    'quantity':
     10,
    'price': 60
    }
    Fruit_Json = json.dumps(Fruit_Dict)


    # userdict ={'usernam':username,
    # 'password':password
    
    # }

    # user_json=json.dumps(userdict)

    print("in /register")
    # session['username']=username
    result=username + ' ' + password + ' ' + role
    # return registration(username,password)
    return redirect(url_for("homepage"))

if __name__ == '__main__':
   app.run(debug = True)


# from flask import Flask, render_template, request

# app = Flask(__name__)

# if __name__ == "__main__":
#     app.run(debug=True)