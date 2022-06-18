
import re
import pytest
@pytest.mark.parametrize("balance",[ (24.4), ("24.4"), (-30.404),(0)

 ])
def test_validate_balance(balance):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(balance,float) or isinstance(balance,int)))
    
    amount_conditional =  (balance>=1 and balance<1000)

    assert amount_conditional_isnum == True, "The amount must be a value"
    assert amount_conditional == True, "The amount must be between 1 and 1000"