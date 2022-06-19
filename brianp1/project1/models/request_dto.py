
class employee_request:
    def __init__(self, employee_id, amount: int, description: str,status: bool):
     self.employee_id = employee_id
     self.amount = amount
     self.description = description
     self.status = status

    def __repr__(self) -> str:
        return f"Employee request: {self.employee_id} + {self.amount} + {self.description} + {self.status}"
