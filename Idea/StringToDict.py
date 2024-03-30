import ast

def convert_string_to_dict(string_data):
    try:
        dict_data = ast.literal_eval(string_data)
        return dict_data
    except ValueError as e:
        print("Invalid string for dictionary conversion: ", e)
        return None

# Test the function
string_data = "{'name': 'John', 'age': 30, 'city': 'New York'}"
dict_data = convert_string_to_dict(string_data)
print(dict_data)