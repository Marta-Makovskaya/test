import db

def print_menu():
    print("Выберите нужную команду:")
    print("0. Выход")
    print("1. Показать список студентов")
    print("2. Показать список преподавателей")
    print("3. Показать список программ")
    print("4. Показать список курсов")
    print("5. Вывести детальную информацию по студенту")

def print_student_details(student_id):
    details = db.get_student_details(student_id)
    if not details:
        print("Студент с таким ID не найден.")
        return

    print("/" * 11)
    print(f"Детальная информация о студенте с ID {student_id}:")
    for detail in details:
        print(f"ID: {detail[0]}, Имя: {detail[1]}, Фамилия: {detail[2]}, Курс: {detail[3]}, Оценка: {detail[4]}")
    print("/" * 11)

def app():
    db.init_db()
    print("Successfully initialized the database.")

    print("Вас приветствует программа онлайн-управления университетом!")
    while True:
        print_menu()
        cmd = int(input("Введите номер команды: "))

        if cmd == 0:
            print("Goodbye!")
            break  # Exit the loop
        elif cmd == 1:
            print("/" * 11)
            print("Список студентов:")
            students = db.get_all_students()
            for student in students:
                print(f"ID: {student[0]} - Полное имя: {student[1]} {student[2]}, email: {student[3]}")
                print("/" * 11)
        elif cmd == 2:
            print("/" * 11)
            print("Список преподавателей:")
            instructors = db.get_all_instructors()
            for instructor in instructors:
                print(f"ID: {instructor[0]} - Полное имя: {instructor[1]} {instructor[2]}, email: {instructor[3]}.")
                print("/" * 11)
        elif cmd == 3:
            print("/" * 11)
            print("Список программ:")
            programs = db.get_all_programs()
            for program in programs:
                print(f"ID: {program[0]} - Название программы: {program[1]}")
                print("/" * 11)
        elif cmd == 4:
            print("/" * 11)
            print("Список курсов:")
            courses = db.get_all_courses()
            for course in courses:
                print(f"ID: {course[0]} - Название курса: {course[1]}")
                print("/" * 11)
        elif cmd == 5:
            print("/" * 11)
            print("Детальная информация по студенту:")
            student_id = int(input("Введите ID студента, информацию о котором хотите получить: "))
            print_student_details(student_id)  # Вызов новой функции
        else:
            print("Неправильная команда, попробуйте снова.")

if __name__ == "__main__":
    app()