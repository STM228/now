import os
import game


def show_menu():
    """
    показывает гавноеменю
    из него взывается функция начала
    из него завершается
    """
    while True:
        os.system("cls")
        print("1 - начать новую игру")
        print("0 -  выйти")
        answer = input("Введите номер ответа и нажмите ENTER: ")
        if answer == "1":
            game.start_game()
            break
        elif answer == "0":
            print("Выходим из игры")
            break

show_menu()
