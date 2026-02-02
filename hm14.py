# 1
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    # 2
    def show_info(self):
        print(f"Студент: {self.name}, Вік: {self.age}, Курс: {self.course}")
    # 3
    def change_course(self, new_course):
        self.course = new_course
        print(f"{self.name} тепер на курсі {self.course}")
student1 = Student("Олександр", 20, "Python")
student2 = Student("Софія", 21, "Java")
student1.show_info()
student2.show_info()
student1.change_course("C++")
student1.show_info()
# 4
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
    def mark_done(self):
        self.completed = True
# 5
task1 = Task("Вивчити Python")
task2 = Task("Прочитати книгу")
task3 = Task("Зробити домашку")
tasks = [task1, task2, task3]
for t in tasks:
    status = "Виконано" if t.completed else "Не виконано"
    print(f"{t.title} - {status}")
task1.mark_done()
for t in tasks:
    status = "Виконано" if t.completed else "Не виконано"
    print(f"{t.title} - {status}")
# 6
class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date
    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}")
event1 = Event("Зустріч з друзями", "2026-02-05")
event1.show()
# 7
class EventExtended(Event):
    def __init__(self, title, date, description=""):
        super().__init__(title, date)
        self.description = description
    def update_description(self, new_description):
        self.description = new_description
    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}, Опис: {self.description}")
event2 = EventExtended("Конференція", "2026-05-02")
event2.update_description("Тема: Нові технології в Python")
event2.show()
