students = [
    {"name": "Гермиона", "age": 17, "grade": 5.0},
    {"name": "Гарри", "age": 17, "grade": 4.2},
    {"name": "Рон", "age": 16, "grade": 3.9},
    {"name": "Люси", "age": 17, "grade": 4.8},
    {"name": "Грегори", "age": 16, "grade": 4.5}
]

def filter_students_by_grade(students_list, min_grade=4.0):
    filtered = [student for student in students_list if student["grade"] >= min_grade]
    return filtered

filtered_students = filter_students_by_grade(students, 4.0)

print("Студенты со средним баллом выше 4.0:")
for student in filtered_students:
    print(f"Имя: {student['name']}, Средний балл: {student['grade']}")