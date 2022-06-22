Project 1
Project Description
This project is a rudimentary expense reimbursement system. This is a single page app (SPA) that allows employees to make reimbursement requests and managers to approve or deny them; managers also have the ability to request reimbursements. The data is persisted on an AWS RDS instance to keep track of user information and requests.

Technologies Used
JavaScript
HTML
CSS
PostgreSQL
Pytest

Features
DOM manipulation through Javascript
RESTful API server
flask sessions to track user data within the SPA

Getting Started
#Create a local git repository using git clone
git clone git@github.com:lago77/project1.git
cd project1
# Start working on the project

# If HTTP is preferred incase an ssh key is not setup
git clone https://github.com/DementedTiger/HeroPay.git
cd HeroPay
Usage
Essential requirements

An RDS system or installed on a local machine
For remote capabilities:

A running RDS instance to host the database
Steps to get it running:
Make sure the RDS instance DB has the SQL scripts ran that generate the required tables
Populate the tables with user logins needed to access the website
Complete.