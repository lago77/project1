class employee_login:
    def __init__(self, employee_id, user_name, user_password):
        self.employee_id = employee_id
        self.user_name = user_name
        self.user_password = user_password

    def __repr__(self) -> str:
        return f"Employee Login : employee id - {self.employee_id} username - {self.user_name} password - {self.user_password}"
    
        