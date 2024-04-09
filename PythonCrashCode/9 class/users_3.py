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

# Main
user_1 = User("John", "Doe", 25, "New York",0)
user_2 = User("Vy Vy", "Nguyen", 18, "Long Xuyen",0)
user_1.describe_user()
user_1.greet_user()
user_1.increment_logon_attempts()
user_1.describe_user()
user_1.reset_logon_attempts()
user_1.describe_user()