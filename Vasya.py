#FIXME ошибка какой та странный исправлять ашибка6 а то па попе



class Humanoid:
    def __init__(self):
        self.hp = 100
        self.name = "Вася Питонов"
        self.damage = 100
        self.mana = 100
        self.armour = 100
        self.money = 600
        self.inventory = []


    def use_poution(self):
        print(self.inventory)
        user_choise = input("Выберете из инвентаря зелья: ")
        if user_choise == "Зелье здоровья":
            if "Зелье здоровья" in self.inventory:
                self.hp = 0
                self.hp += 100
                print("Здороья востановлено")
            else:
                print("У тебя нет зелья здоровья")
        elif user_choise == "Зелье маны":
            if "Зелье маны" in self.inventory:
                self.mana = 0
                self.mana += 100
                print("Мана востановлена")
            else:
                print("У тебя нет зелья здоровья")
    
    def show_stats():
        pass

def fight(player, enemy) -> None:
    while player.hp > 0 and enemy.hp > 0:
        print("Воин атаковал мага и нанес {}. Здоровье мага: {}".format(player.damage - enemy.armour, enemy.hp))
        if enemy.hp <= 0:
            break

        print("Маг нанес воину {} урона. Здоровье воина: {}".format(enemy.damage - player.armour, player.hp))

        if player.hp <= 0:
            print("Враг победил")
        else:
            print("Игрок победил")



def visit_shop(player) -> None:
    text = "Он наконец то зашел в продуктовый, прокричал продавец. Здесь много чего продается и на полу спит алкаш."
    options = [
        "0 - Купить зелье здоровья за 100 монет",
        "1 - Купить зелье маны за 150 монет",
        "2 - Уйти на Арбат"
    ]
    print(text)
    choise_user = input(options)
    if choise_user == "0":
        if player.money >= 100:
            print("В инвентарь добавлено зелье здоровья")
            player.inventory.append("Зелье здоровья")
        else:
            print("Деняг нема у тебя братишка")
    elif choise_user == "1":
        if player.money >= 150:
            print("В инвентарь добавлено зелье маны")
            player.inventory.append("Зелье маны")
        else:
            print("Деняг нема у тебя братишка")
    else:
        print("Братиш, сорян Арбат еще не открыли")

    
player = Humanoid()
enemy = Humanoid()

fight(player, enemy)