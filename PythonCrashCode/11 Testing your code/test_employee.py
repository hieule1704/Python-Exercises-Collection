from employee import Employee

def test_give_default_raise():
    my_employee = Employee('John', 'Doe',10000)
    my_employee.give_raise()
    assert my_employee.annualy_salary == 15000

def test_give_custome_raise():
    my_employee = Employee('John', 'Doe',10000)
    my_employee.give_raise(10000)
    assert my_employee.annualy_salary == 20000