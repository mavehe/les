import random
#Створення персонажу
def create_player():
    name = input("Введіть імʼя героя: ")
    while True:
        try:
            print("Оберіть клас:")
            print("1 — Воїн (багато здоровʼя)")
            print("2 — Мисливець (збалансований)")
            print("3 — Маг (мало здоровʼя, сильна атака)")
            choice = int(input("Ваш вибір: "))
            if choice == 1:
                return {"name": name, "hp": 120, "attack": 15, "gold": 10}
            elif choice == 2:
                return {"name": name, "hp": 100, "attack": 12, "gold": 15}
            elif choice == 3:
                return {"name": name, "hp": 80, "attack": 20, "gold": 20}
            else:
                print("Неправильний вибір")
        except ValueError:
            print("Введіть число!")
#Статус героя
def show_status(player):
    print("СТАТУС ГЕРОЯ")
    print(f"Імʼя: {player['name']}")
    print(f"Здоровʼя: {player['hp']}")
    print(f"Атака: {player['attack']}")
    print(f"Золото: {player['gold']}")
#Бій
def fight(player):
    enemy_hp = random.randint(30, 60)
    enemy_attack = random.randint(5, 12)
    print("ПОЧАВСЯ БІЙ!")
    while enemy_hp > 0 and player["hp"] > 0:
        print(f"Здоровʼя ворога: {enemy_hp}")
        print("1 — Атакувати")
        print("2 — Захищатися")
        print("3 — Втекти")
        try:
            action = int(input("Ваш вибір: "))
            if action == 1:
                damage = random.randint(5, player["attack"])
                enemy_hp -= damage
                print(f"Ви нанесли {damage} шкоди!")
            elif action == 2:
                reduced_damage = enemy_attack // 2
                player["hp"] -= reduced_damage
                print(f"Ви захистились і отримали {reduced_damage} шкоди")
            elif action == 3:
                print("Ви втекли з бою")
                return
            else:
                print("Невірна команда")
            if enemy_hp > 0:
                player["hp"] -= enemy_attack
                print(f"Ворог атакує і завдає {enemy_attack} шкоди")
        except ValueError:
            print("Введіть число!")
    if player["hp"] > 0:
        reward = random.randint(5, 15)
        player["gold"] += reward
        print(f"Перемога! Ви отримали {reward} золота")
    else:
        print("Ви загинули в бою")
#Вибір дії
def choose_action():
    print("Оберіть дію:")
    print("1 — Дослідити місцевість")
    print("2 — Переглянути статус")
    print("3 — Вийти з гри")
    try:
        return int(input("Ваш вибір: "))
    except ValueError:
        return 0
#Кінець гри
def end_game(player):
    print("ГРА ЗАВЕРШЕНА")
    show_status(player)
    if player["hp"] <= 0:
        print("Кінцівка: Ви загинули.")
    elif player["gold"] >= 50:
        print("Кінцівка: Ви розбагатіли та стали легендою!")
    else:
        print("Кінцівка: Ви вижили, але світ залишився незмінним.")
#Головна функція
def main():
    print("ЛАСКАВО ПРОСИМО ДО ТЕКСТОВОЇ RPG")
    player = create_player()
    game_running = True
    while game_running and player["hp"] > 0:
        action = choose_action()
        if action == 1:
            if random.choice([True, False]):
                fight(player)
            else:
                print("Ви нічого не знайшли")
        elif action == 2:
            show_status(player)
        elif action == 3:
            game_running = False
        else:
            print("Невірний вибір")
    end_game(player)
#Запуск гри
main()

