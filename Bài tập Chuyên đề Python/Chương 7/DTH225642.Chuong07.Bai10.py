import json


classes = {}


def add_class(class_id, class_name):
    classes[class_id] = {'class_name': class_name, 'students': {}}


def add_student(class_id, student_id, student_name, birth_year):
    if class_id in classes:
        classes[class_id]['students'][student_id] = {
            'student_name': student_name,
            'birth_year': birth_year
        }


def delete_student(class_id, student_id):
    if class_id in classes and student_id in classes[class_id]['students']:
        del classes[class_id]['students'][student_id]


def edit_student(class_id, student_id, new_name, new_birth_year):
    if class_id in classes and student_id in classes[class_id]['students']:
        classes[class_id]['students'][student_id]['student_name'] = new_name
        classes[class_id]['students'][student_id]['birth_year'] = new_birth_year


def search_students(search_name):
    result = {}
    for class_id, class_info in classes.items():
        for student_id, student_info in class_info['students'].items():
            if search_name.lower() in student_info['student_name'].lower():
                if class_id not in result:
                    result[class_id] = {}
                result[class_id][student_id] = student_info
    return result


def sort_students(class_id):
    if class_id in classes:
        sorted_students = sorted(classes[class_id]['students'].items(), key=lambda x: x[1]['student_name'])
        return sorted_students
    return []


def save_to_json(file_path):
    with open(file_path, 'w') as f:
        json.dump(classes, f, indent=4)


def load_from_json(file_path):
    global classes
    with open(file_path, 'r') as f:
        classes = json.load(f)


def main():
    add_class('101', 'Chuyên đề Python')
    add_student('101', '001', 'Huỳnh Nhựt Phát', 2004)
    add_student('101', '002', 'Lê Nhật Quang', 2004)
    edit_student('101', '002', 'Lê Nhật Trí', 2004)
    delete_student('101', '001')
    print(search_students('Trí'))
    print(sort_students('101'))
    save_to_json('students.json')
    load_from_json('students.json')

if __name__ == "__main__":
    main()
