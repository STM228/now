import os


def show(player:tuple) -> tuple:
    name = player[5]
    money = player[6]
    while True:

        os.system("cls")
        print(f"{player[0]} Приехал в лавку алхимика")
        print("Имя персонажа ",name)
        print("Деньги персонажа ",money)
        print("Жизни перснажа ",hp)
        print("Зелья в инвентаре ",potions)
        print("1 - купить зелье")
        print("2 - уехать обратно к камню")


        answer = input("\n Введите номер варианта и нажмите ENTER")
        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10
                potions += 1
                print("Купили зелье за 10 монет")
                input("пауза в магазине")
            else:
                print("Недостаточно монет!")
                input("\nНажмите ENTER чтобы продолжить: ")
        elif answer == "2":
            return (player[0],player[1], player[2], player[3], money, potions)
        input("\nНажмите ENTER чтобы продолжить: ")
