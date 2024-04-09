from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, location,logon_attempts,privileges):
        super().__init__(first_name, last_name, age, location,logon_attempts)
        self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
# Main
"""
admin_1 = Admin("John", "Doe", 25, "New York",0,["can add post","can delete post","can ban user"])
admin_1.describe_user()
admin_1.privileges.show_privileges()

"""