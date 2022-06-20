def validate_amount(amount):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(amount,float) or isinstance(amount,int)))
    
    amount_conditional =  (amount>=1 and amount<1000)

    assert amount_conditional_isnum == True, "The amount must be a value"
    assert amount_conditional == True, "The amount must be between 1 and 1000"

    if (amount_conditional and amount_conditional):
        return True
    else:
        return False