students = [
    {"name": "Гермиона", "age": 17, "avg_grade": 5.0},
    {"name": "Гарри", "age": 17, "avg_grade": 4.2},
    {"name": "Рон", "age": 16, "avg_grade": 3.9},
    {"name": "Люси", "age": 17, "avg_grade": 4.8},
    {"name": "Грегори", "age": 16, "avg_grade": 4.5}
]

filtered_students = [student for student in students if student["avg_grade"] > 4.0]


print("Студенты со средним баллом выше 4.0:")
for student in filtered_students:
    print(f"Имя: {student['name']}, Средний балл: {student['avg_grade']}")