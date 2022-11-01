
import os

def show(player_name, player_hp, player_money, player_potions):
    while True:
        os.system("cls")
        print(f"{player_name} Приехал в лавку алхимика")
        print("Имя персонажа ",player_name)
        print("Деньги персонажа ",player_money)
        print("Жизни перснажа ",player_hp)
        print("Зелья в инвентаре ",player_potions)
        print("1 - купить зелье")
        print("2 - уехать обратно к камню")
        answer = input("\n Введите номер варианта и нажмите ENTER")
        if answer == "1":
            os.system("cls")
            if player_money >= 10:
                player_money -= 10
                player_potions += 1
                print("Купили зелье за 10 монет")
                input("пауза в магазине")
            else:
                print("Недостаточно монет!")
                input("\nНажмите ENTER чтобы продолжить: ")
        elif answer == "2":
            break
        input("\nНажмите ENTER чтобы продолжить: ")