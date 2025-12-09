from src.lab09.group import Group
from src.lab08.models import Student


def main():
    path = "data/lab09/students.csv"
    group = Group(path)

    print("Изначальный список")
    for s in group.list():
        print("  ", s)

    print("Добавление студента")
    new_student = Student(
        fio="Тестовый Студент",
        birthdate="2007-05-11",
        group="БИВТ-25-4",
        gpa=4.7
    )
    group.add(new_student)
    print("Добавлен:", new_student)

    print("Проверка списка после добавления")
    for s in group.list():
        print("  ", s)

    print("Поиск студента по ФИО")
    found = group.find("Тест")
    for s in found:
        print("найден:", s)

    print("Обновление GPA")
    group.update("Тестовый Студент", gpa=5.0)
    print("GPA обновлён.")

    print("Список после обновления")
    for s in group.list():
        print("  ", s)

    print("Удаление")
    group.remove("Тестовый Студент")
    print("Удалён Тестовый Студент")

    print("Финальный список")
    for s in group.list():
        print("  ", s)


if __name__ == "__main__":
    main()