import json

def convert_string_to_json(string_data):
    try:
        json_data = json.loads(string_data)
        return json_data
    except ValueError as e:
        print("Invalid string for JSON conversion: ", e)
        return None

# Test the function
string_data = '{"name": "John", "age": 30, "city": "New York"}'
json_data = convert_string_to_json(string_data)
print(json_data)