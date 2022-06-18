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


@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    # print("in dashboard")
    # print(data)
    # mydata=json.loads(data)
    # print("mydata")
    # print(mydata)
    # return my_dashboard(mydata)
    print("in dashboard")
    print(request.args)
    # print(type(request.args['userdata']))
    username=request.args['username']
    password=request.args['password']
    print
    print("hi")
    return my_dashboard(username,password)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('registration.html')

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
    print(request.data)
    # Response = flask.jsonify(request.data)
    # Response.headers.add('Access-Control-Allow-Origin', '*')
    # mydict={"value":id, "value2":status}
    return makerequest(request.data)



@app.route('/update_request/',methods=['POST','GET'])
def updatereq():
    
    print("my data")
    data="test"
    print("my request")
    print(request.data)
    # mydict={"value":id, "value2":status}
    return updaterequest(request.data)



@app.route('/delete_request/',methods=['DELETE'])
def deletereq():
    
    print("my data")
    data="test"
    print("my request")
    print(request.data)
    # mydict={"value":id, "value2":status}
    return deleterequest(request.data)


@app.route('/get_request/<id>',methods=['GET'])
def get_req(id):
    print("in getreq")
   
    return getrequest(id)
# @app.route('/update_request/<id>',methods=['POST'])
# def delete_request(id):
#     return deleterequest(id)

# @app.route('/requests/<id>',methods=['GET'])
# def requests(id):
#     return get_requests(id)

# @app.route('/anothers', methods=['POST','GET'])
# def another():
#     print("in anothers")
#     return my_another()

@app.route('/nextpage')
@app.route('/login',methods = ['POST', 'GET'])
def login():
   print("the request is in login")
   print(request.data)
   mydata=json.loads(request.data)
   userdata="sdfsd"
   if request.method == 'POST':
      print("in post")
      print(mydata)
      print(type(mydata))
    #   user = request.form['name']
    #   session['name']=user
    #   session['email']=request.form['email']
      return redirect(url_for('dashboard',username=mydata['username'],password=mydata['password']))
#    else:
#     #   user = request.args.get('name')
#       return render_template('login.html')


@app.route('/register',methods = ['POST'])
def register():


    # username = request.form['username']
    # password = request.form['password']
    print("my request")
    print("round two")
    print(request.form)

    username=request.form['username']
   
    password=request.form['password']
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
    result=username + ' ' + password
    # return registration(username,password)
    return result

if __name__ == '__main__':
   app.run(debug = True)


# from flask import Flask, render_template, request

# app = Flask(__name__)

# if __name__ == "__main__":
#     app.run(debug=True)