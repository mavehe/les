#1
from datetime import datetime
text = input("Що сьогодні сталося? ")
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(f"{datetime.now()} — {text}")
print("Запис збережено!")
#2
with open("grades.txt", "r", encoding="utf-8") as file:
    grades = [int(line) for line in file]
average = sum(grades) / len(grades)
print("Середня оцінка:", average)
#3
import os
filename = "data.txt"
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
else:
    print("Файл не знайдено")
#4
a = float(input("Введи число 1: "))
b = float(input("Введи число 2: "))
result = a + b
with open("calc_history.txt", "a", encoding="utf-8") as file:
    file.write(f"{a} + {b} = {result}")
print("Результат:", result)
#5
a = float(input("Введи число 1: "))
b = float(input("Введи число 2: "))
result = a + b
with open("calc_history.txt", "a", encoding="utf-8") as file:
    file.write(f"{a} + {b} = {result}")
print("Результат:", result)
#6
import json
event = input("Назва події: ")
date = input("Дата: ")
data = []
try:
    with open("planner.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    pass
data.append({"event": event, "date": date})
with open("planner.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
print("Подію збережено")
#7
with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = [int(line) for line in file]
numbers.sort()
print("Відсортовані числа:", numbers)
