#1
while True:
    try:
        number = int(input("Введи число: "))
        print("Ти ввів правильно:", number)
        break
    except ValueError:
        print("Це не число, спробуй ще раз")
#2
print("1 - +")
print("2 - -")
print("3 - *")
print("4 - /")
try:
    choice = int(input("Вибери операцію: "))
    a = float(input("Введи перше число: "))
    b = float(input("Введи друге число: "))

    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)
    elif choice == 4:
        print(a / b)
    else:
        print("Невірний вибір")
except ValueError:
    print("Потрібно вводити числа")
except ZeroDivisionError:
    print("Ділення на нуль заборонено")
#3
name = input("Введи імʼя: ")
try:
    age = int(input("Введи вік: "))
    if 1 <= age <= 120:
        print(f"Привіт, {name}, тобі {age} років")
    else:
        print("Вік має бути від 1 до 120")
except ValueError:
    print("Вік має бути числом")
#4
numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Введи індекс (0-4): "))
    print("Значення:", numbers[index])
except ValueError:
    print("Індекс має бути числом")
except IndexError:
    print("Неправильний індекс")
#5
try:
    file = open("text.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Файл не знайдено")
#6
RATE = 40  
try:
    usd = float(input("Введи суму в USD: "))
    print("UAH:", usd * RATE)
except ValueError:
    print("Неправильний ввід")
#7
try:
    a = int(input("Введи число: "))
    b = int(input("Введи друге число: "))
    print("Результат:", a / b)
except ValueError:
    print("Потрібно вводити числа")
except ZeroDivisionError:
    print("Не можна ділити на нуль")
except Exception:
    print("Невідома помилка")
