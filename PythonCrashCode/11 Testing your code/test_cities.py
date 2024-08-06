from city_funtions import formated_city_country

def test_city_country():
    """Does 'Ho Chi Minh, Viet Nam' work?"""
    formated_name = formated_city_country("ho chi minh", "vietnam")
    assert formated_name == "Ho Chi Minh, Vietnam"

def test_city_country_population():
    """Does 'Santiago, Chile - population 5000000' work?"""
    formated_name = formated_city_country("Santiago", "chile", 5000000)
    assert formated_name == "Santiago, Chile - Population 5000000"
