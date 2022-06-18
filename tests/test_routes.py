
import re
import pytest


def test_get_login():
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    balance_conditional_isnum= ((isinstance(balance,float) or isinstance(balance,int)))
    
    balance_conditional_ispositive =  (balance>=0)

    assert balance_conditional_ispositive == True, "Your balance must not be negative"

