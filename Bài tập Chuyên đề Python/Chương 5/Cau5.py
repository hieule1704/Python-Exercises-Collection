# Xu ly tach chuoi
def input_string(string_store):
    while True:
        char = input("Enter your number, enter 'quit' to quit: ")
        if char == 'quit':
            return ';'.join(string_store) # Hàm join chỉ join kiểu dử liệu chuổi, join int sẽ lỗi
        else:
            string_store.append(char)

def check_character(string):
    list_string = string.split(';')
    uppercaseCount = 0
    lowercaseCount = 0
    digitCount = 0
    specialCharCount = 0
    whitespaceCount = 0
    vowelCount = 0
    consonantCount = 0
    for char in list_string:
        if char.isupper():
            uppercaseCount += 1
        elif char.islower():
            lowercaseCount += 1
        elif char.isdigit():
            digitCount += 1
        elif char.isspace():
            whitespaceCount += 1
        else:
            specialCharCount += 1
        if check_vowel(char):
            vowelCount += 1
        elif check_consonant(char):
            consonantCount += 1

    print(f"Uppercase: {uppercaseCount}\n"
          f"Lowercase: {lowercaseCount}\n"
          f"Digit: {digitCount}\n"
          f"Special Character: {specialCharCount}\n"
          f"Whitespace: {whitespaceCount}\n"
          f"Consonant: {consonantCount}\n"
          f"Volve: {vowelCount}")


def check_vowel(char):
    vowel_ascii_value = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117] # [A, E, I, O, U, a, e, i, o, u]
    if ord(char) in vowel_ascii_value:
        return True
    return False

def check_consonant(char):
    vowel_ascii_value = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]  # [A, E, I, O, U, a, e, i, o, u]
    if ord(char) in range(65,91) or ord(char) in range(97,123):
        if ord(char) not in vowel_ascii_value:
            return True
    return False

def main():
    string_store = []
    string_store = input_string(string_store)
    check_character(string_store)

if __name__ == '__main__':
    main()

"""
    ChatGPT:
uppercaseCount = 0
lowercaseCount = 0
digitCount = 0
specialCharCount = 0
whitespaceCount = 0
vowelCount = 0
consonantCount = 0

# Ví dụ xử lý một chuỗi
text = "Hello, World!"

for char in text:
    if char.isupper():
        uppercaseCount += 1
    elif char.islower():
        lowercaseCount += 1
    elif char.isdigit():
        digitCount += 1
    elif char.isspace():
        whitespaceCount += 1
    elif char in "!@#$%^&*()_+-=[]{}|;:',.<>?/`~":
        specialCharCount += 1
    if char.lower() in 'aeiou':
        vowelCount += 1
    elif char.lower() in 'bcdfghjklmnpqrstvwxyz':
        consonantCount += 1

print("Uppercase Count:", uppercaseCount)
print("Lowercase Count:", lowercaseCount)
print("Digit Count:", digitCount)
print("Special Character Count:", specialCharCount)
print("Whitespace Count:", whitespaceCount)
print("Vowel Count:", vowelCount)
print("Consonant Count:", consonantCount)
"""