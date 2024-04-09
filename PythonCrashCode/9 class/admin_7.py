class User:
    def __init__(self, first_name, last_name, age, location,logon_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.logon_attempts = logon_attempts

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}.")
        print(f"Longon attempts: {self.logon_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_logon_attempts(self):
        self.logon_attempts += 1
    def reset_logon_attempts(self):
        self.logon_attempts = 0

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
admin_1 = Admin("John", "Doe", 25, "New York",0,["can add post","can delete post","can ban user"])
admin_1.describe_user()
admin_1.privileges.show_privileges()