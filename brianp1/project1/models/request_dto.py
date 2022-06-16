
class employee_request:
    def __init__(self, employee_id, amount: int, description: str, request_approval: bool, request_cancellation: bool, request_pending: str, employee_position: str):
     self.employee_id = employee_id
     self.amount = amount
     self.description = description
     self.request_approval = request_approval
     self.request_cancellation = request_cancellation
     self.request_pending = request_pending
     self.employee_position = employee_position
    

    def __repr__(self) -> str:
        return f"Employee request: {self.employee_id} + {self.amount} + {self.description} + {self.request_approval} + {self.request_cancellation} + {self.request_pending} + {self.employee_position}"
