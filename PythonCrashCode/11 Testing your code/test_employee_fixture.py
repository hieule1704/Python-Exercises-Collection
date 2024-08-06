import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee('John', 'Doe', 12000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annualy_salary==17000

def test_give_custome_raise(employee):
    employee.give_raise(10000)
    assert employee.annualy_salary==22000