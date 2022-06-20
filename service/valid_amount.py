def validate_amount(amount):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(amount,float) or isinstance(amount,int)))
    print("amount is",amount)
    print("conditional,", amount_conditional_isnum)
    if (amount_conditional_isnum==True):
        amount_conditional =  (amount>=1 and amount<1000)
    else:
        amount_conditional =  False

    if (amount_conditional and amount_conditional_isnum):
        return True
    else:
        return False