from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request, session
from controllers.dashboard import *
app = Flask(__name__)

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    return my_dashboard()
   #  return render_template('dashboard.html',name=name)
#    return 'welcome %s' % name

# def initializing_account():
#     print("in account/creation")
#     # print(request.query_string)
#     print(request.form)
#     return processing_account(request.form)
app.secret_key = 'BAD_SECRET_KEY'
# @app.route('/another/<name>', methods=['POST','GET'])
# def another(name):
    
#    #  print(request.form)
#     print("in anothers")
#     print("my name")
#     print(name)
    
#     return my_another(name)

@app.route('/anothers', methods=['POST','GET'])
def another():
    print("in anothers")
    return my_another()


@app.route('/nextpage')
@app.route('/login',methods = ['POST', 'GET'])
def login():
   print("the request is")
   print(request)
   print(request.method)
   if request.method == 'POST':
      user = request.form['name']
      session['name']=user
      session['email']=request.form['email']
      return redirect(url_for('dashboard'))
   else:
      user = request.args.get('name')
      return render_template('login2.html')

if __name__ == '__main__':
   app.run(debug = True)


# from flask import Flask, render_template, request

# app = Flask(__name__)

# if __name__ == "__main__":
#     app.run(debug=True)