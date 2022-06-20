class Requests:

    def __init__ (self, request_id, user_id, description, amount, status):
        self.request_id=request_id
        self.user_id = user_id
        self.description= description
        self.amount = amount
        self.status = status

    def __repr__(self):

        return f"User Info: User id: {self.user_id} || Request ID: {self.request_id} || Description: {self.description} || Amount: {self.amount} || Status: {self.status}"