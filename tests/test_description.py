
import re
import pytest
@pytest.mark.parametrize("description",[ ("sdfasdfs asdfasdfsdfsdfs"), ("sdfsdfsdfsdf sfdasdfsadfsd faf asdfsdfsfsdfsdf"), ("sdfsdf"),("sdfsdfsdfsfsd")

 ])
def test_validate_balance(description):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    description_conditional = (len(description)>=100)
    

    assert description_conditional != True, "The description must be atleast 100 characters in length"


####### test for failure too