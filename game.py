import os
import shop
import hero_engine

def make_hero(name="Безымянный", hp=1, money=0, potion=0) -> tuple:
    return(name, hp, money, potion)


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
    player = hero_engine.make_hero()

    # TODO: щтправить в хиро енгин
    player_name = input("Введите имя ")
    player_money = 50
    player_hp = 100
    player_xp = 0
    player_potions = 0
    player = (player_name, player_hp, player_money, player_potions)

    n_player_name = "Ган ган"
    n_player_money = 50
    n_player_hp = 100
    n_player_potions = 0

    is_game = True
    while is_game:
        os.system("cls")
        print(f"имя: {player[0]}")
        print(f"деньги: {player[1]}")
        print(f"здоровье: {player[2]}")
        print(f"зелья: {player[3]}")

        print(f"{player_name} приехал к камню")
        print("1 - поехать на битву с разбойниками ")
        print("2 - роехать играть в кости")
        print("3 - поехать в лавку алхимика")

        answer = input("Введите номер ответа и нажмите ENTER")
        if answer == "1":
            print("разбойники")
        elif answer == "2":
            print("поехал играть в кости")
        elif answer == "3":
            player = shop.show(player)
        input("Нажмите ENTER чтобы продолжить")