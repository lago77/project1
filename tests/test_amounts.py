
import re
import pytest
@pytest.mark.parametrize("amount",[ (1.5), (200), (999),(999.90)

 ])
def test_validate_amount(amount):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(amount,float) or isinstance(amount,int)))
    
    amount_conditional =  (amount>=1 and amount<1000)

    assert amount_conditional_isnum == True, "The amount must be a value"
    assert amount_conditional == True, "The amount must be between 1 and 1000"



######### test for invalid balance
@pytest.mark.parametrize("amount",[ (2000), ("24.4"), (-30.404),(0)

 ])
def test_invalidate_balance(amount):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(amount,float) or isinstance(amount,int)))
    print("amount is",amount)
    print("conditional,", amount_conditional_isnum)
    if (amount_conditional_isnum==True):
        amount_conditional =  (amount>=1 and amount<1000)
    else:
        amount_conditional =  False

    # assert amount_conditional_isnum != True, "The amount must be a value"
    assert (amount_conditional and amount_conditional_isnum) != True, "The amount must be between 1 and 1000 or a value"