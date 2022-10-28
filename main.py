import os
import shop

def show_menu():
    """
    показывает гавноеменю
    из него взывается функция начала
    из него завершается



    """
    while True:
        os.system("cls")
        print("1 - начать новую игру")
        print("2 -  выйти")
        answer = input("Введите номер ответа и нажмите ENTER")
        if answer == "1":
            start_game()
            break
        elif answer == "2":
            print("Выходим из игры")
            break


    print("пока")


def start_game():
    """
    создает персонажа:
        player_name - имя игрока
        player_money -  деньги игрока
        player_hp - жизни игрока,>
        player_xp - опыт игрока
        player_potions - зелья которые что то дают
    деньги
    имя
    запускает игру
    игра контролируется переменной is_game

    """

    player_name = input("Введите имя ")
    player_money = "50"
    player_hp  = "100"
    player_xp = "0"
    player_potions = 0

    is_game = True
    while is_game:
        os.system("cls")
        print(f"имя: {player_name}")
        print(f"деньги: {player_money}")
        print(f"здоровье: {player_hp}")
        print(f"опыт: {player_xp}")
        print(f"{player_potions}")
        print(f"{player_name} приехал к камню")
        print("1 - поехать на битву с разбойниками ")
        print("2 - роехать играть в кости")
        print("3 - поехать в лавку алхимика")
        answer = input("Введите номер ответа и нажмите ENTER")
        if answer == "1":
            print("поехал на битву")
        elif answer == "2":
            print("поехал играть в кости")
        elif answer == "3":
            shop.shop(player_name, player_money, player_hp, player_xp, player_potions)
        input("Нажмите ENTER чтобы продолжить")

show_menu()
