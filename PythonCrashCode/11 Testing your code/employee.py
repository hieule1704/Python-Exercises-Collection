class Employee:
    def __init__(self, first_name, last_name, annualy_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annualy_salary = annualy_salary

    def give_raise(self, ammount=5000):
        self.annualy_salary += ammount
    