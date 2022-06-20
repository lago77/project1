
from sqlalchemy import true


def validate_description(description):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    description_conditional = (len(description)<=100)

    if description_conditional==True:
        return False
    else:
        return False