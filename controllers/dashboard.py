from django.shortcuts import render
from flask import render_template, redirect,url_for, request, session
import json

from repository.userlogin_dao import select_user_by_username
def my_dashboard(username, password):
   print("my request")
   print("my username is")
   # print(session['name'])

   myname="i'm testing this again"
   myobject=["hey", 1, "now again"]
   # mydata=json.loads(data)
   
   print("mydata in dashboard")
   
   myuser=select_user_by_username(username)
   print("my user")
   print(myuser)
   myuserid=myuser.user_id
   mydict={'username':username, 'password':password, "userid":myuserid}
   return mydict
   # return render_template('dashboard.html',mydict=mydict)

