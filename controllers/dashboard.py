from django.shortcuts import render
from flask import render_template, redirect,url_for, request, session

def my_dashboard():
   print("my request")
   print("my username is")
   print(session['name'])


   return render_template('dashboard.html')

def my_another():

    print("testing")
    print("my name")
    print(session['name'])
    return render_template('another.html')
    # return redirect(url_for('anothers',name = name))