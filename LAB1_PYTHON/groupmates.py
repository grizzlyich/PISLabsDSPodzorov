groupmates = [
    {"name": "Вячеслав", "group": "<БСТ2257>", "age": 24, "marks": [4, 3, 5, 5, 4]},
    {"name": "Дмитрий", "group": "БСТ2257", "age": 24, "marks": [5, 5, 5, 5, 4]},
    {"name": "Александр", "group": "БСТ2257", "age": 24, "marks": [3, 5, 4, 3, 5]},
    {"name": "Сергей", "group": "БСТ2257", "age": 24, "marks": [4, 5, 5, 4, 5]},
]

def print_students(students):
    print("Имя студента".ljust(15),
          "Группа".ljust(8),
          "Возраст".ljust(8),
          "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["group"].ljust(8),
              str(student["age"]).ljust(8),
              str(student["marks"]).ljust(20))
    print()

def average(student):
    return sum(student["marks"]) / len(student["marks"])

def filter_students(students, min_avg):
    return [s for s in students if average(s) > min_avg]

if __name__ == "__main__":
    print_students(groupmates)
    print("Студенты со средним баллом > 4.0:")
    print_students(filter_students(groupmates, 4.0))
