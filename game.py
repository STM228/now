import os
import shop

def start_game():
    os.system("cls")

while True:
    os.system("cls")

    player_name = input("Введите имя ")
    player_money = 100
    player_hp = 100
    player_xp = 50
    player_potions = 1

    print("игра началась")
    print("Персонаж:")
    print(player_name)
    print(player_money, "денег")
    print(player_hp, "жизней")
    print(player_potions, "зелей")

    print("1 - поехать в лавку алхимика")
    print("0 - выйти в главное меню")
    answer = input("\n Введите номер варианта и нажмите ENTER: ")
    if answer == "1":
        shop.show(player_name, player_money, player_hp, player_potions)




