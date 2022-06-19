
import re
import pytest
from repository.userlogin_dao import *

from models.login_dto import Login
from repository.requests_dao import *

# @pytest.mark.parametrize("username, password, role",[ ("omar", "asdfasd3fsdfsdfs", "Manager"), ("Mark", "sfdas3dfsadf", "Employee"), ("Anthony", "df3s", "Employee"),("Marko","sdfsdfs","Manager")

#  ])
# def test_insert_user(username, password,role):
#     ##this function tests to make sure the balance is not negative or and not a string when entered.
    
#     id=insert_user(username,password,role)
    
#     id_int=int(id)
#     id_int_conditional = (type(id_int)==int)
#     print("hi")

#     assert id_int_conditional == True, "Insertion failed, no id returned"

# @pytest.mark.parametrize("id",[ (1), (2),(3),(4), (5)
#  ])
# def test_select_user(id):

#     user=select_user_by_id(id)

#     user_conditional=isinstance(user,Login)

#     assert user_conditional !=True, "User selection failed"


# @pytest.mark.parametrize("user_id, description, amount",[ (1, "asdfasd3fsdfsdfs", 100), (2, "sfdas3dfsadfsd faf asdfsdfsfsd3fsdf",100), (3,"sd3fs", 10),(4,"sdfsdf3sd",30)

#  ])
# def test_insert_request(user_id, description, amount):
#     ##this function tests to make sure the balance is not negative or and not a string when entered.
    
#     id=insert_request(user_id,description,amount)
    
#     id_int=int(id)
#     id_int_conditional = (type(id_int)==int)
#     print("hi")

#     assert id_int_conditional == True, "Insertion failed, no id returned"

# @pytest.mark.parametrize("request_id, status",[ (1, "Denied"), (2, "Approved"), (3, "Approved")


#  ])
# def test_update_request(request_id,status):
#     ##this function tests to make sure the balance is not negative or and not a string when entered.
    
#     newstatus=update_request(request_id, status)
    
#     status_conditional= (newstatus==status)
#     print("hi")

#     assert status_conditional == True, "Update status failed"