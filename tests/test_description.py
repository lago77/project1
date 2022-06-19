
import re
import pytest
@pytest.mark.parametrize("description",[ ("sdfasdfs asdfasdfsdfsdfs"), ("sdfsdfsdfsdf sfdasdfsadfsd faf asdfsdfsfsdfsdf"), ("sdfsdf"),("sdfsdfsdfsfsd")

 ])
def test_validate_description(description):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    description_conditional = (len(description)<=100)
    

    assert description_conditional == True, "The description must be atleast 100 characters in length"


####### test for failure too

@pytest.mark.parametrize("description",[ (" Test test, test test Test test, test testst Test test, test test Test test, test test Test test, test test Test test, test test"), 


(" Visual Studio Code is a text editor that makes viewing and modifying code simple. However, this actually leads to its greatest benefit "), 
("Intellij Community Edition (Optional): Intellij community edition is an excellent Java focused IDE. Make sure to install the community edition instead of the ultimate as that begins with a free trial and")

 ])
def test_invalidate_description(description):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    description_conditional = (len(description)<=100)
    

    assert description_conditional != True, "The description must be atleast 100 characters in length"
