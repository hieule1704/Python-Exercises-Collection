from Cau6 import check_next_number
def test_check_next_number():
    string = '123abc'
    num = check_next_number(string)
    assert num == 123