from random import choice, randint
import os


first_name = ("Жран","Дрын", "Жлыг")
last_name = ("Кривой", "Злопаметный", "Дикий")



def make_hero(
        name=None,
        hp_max=None,
        hp_now=None,
        lvl=1,
        xp_next=None,
        xp_now=0,
        attack=1,
        defence=0,
        weapon=None,
        shield=None,
        luck=1,
        money=None,
        inventary=None,

) -> list:
    if not name:
        name = f"{choice(first_name)} {choice(last_name)}"


    if not hp_now:
        hp_now = randint(1, 100)

    hp_max = hp_now
    xp_next = lvl * 1000

    if money is None:
        money = randint(1, 100)

    if not inventary:
        inventary = []


    """
    Герой это список
    [0] name - имя персонажа
    [1] hp_max - жизнь максимум
    [2] hp_now - текущее кол во жизней
    [3] lvl - уровень персонажа
    [4] xp_nex - опыта для след уровня
    [5] xp_now - текущий опыт
    [6] attack - сила атаки
    [7] defence - защита
    [8] weapon - оружие
    [9] shield - щит
    [10] luck - удача
    [11] money - деньги
    [12] inventary - инвентарь список

    """

    return [
        name,
        hp_max,
        hp_now,
        lvl,
        xp_next,
        xp_now,
        attack,
        defence,
        weapon,
        shield,
        luck,
        money,
        inventary
    ]


def show_hero(hero: str) -> None:
    print("Имя:", hero[0])
    print("жизни:", hero[2], "/", hero[1])
    print("уровень:", hero[3])
    print("опыт:", hero[5], "/", hero[4])
    print("до следующего уровня нужно:", hero[4])
    print("атака:", hero[6])
    print("защита:", hero[7])
    print("оружие:", hero[8])
    print("щит:", hero[9])
    print("деньги:", hero[11])
    print("удача:", hero[10])
    print("инвентарь:", hero[12])
    print("")

def levelup(hero):
    while hero[5] >= hero[4]:
        hero[3] += 1
        hero[4] = hero[3] * 1000
        print(f"{hero[0]} получил {hero[3]} уровень\n")


def buy_item(hero: list, item, price: int) -> None:
    """проверяет есть ли price денег у героя,
     и если есть отнимает из денег героя price,
     и добавляет в инвентарь героя этот item
    """
    os.system("cls")
    if hero[11] >= price:
        hero[11] -= price
        hero[12].append(item)
        print(f"{hero[0]} купил {item} за {price} монет")
    else:
        print(f"{hero[0]} не хватило {price - hero[11]} монет ")
    input("\n Нажмите ENTER чтобы продолжить от магазина")


def consume_item(hero: list, idx: str) -> None:
    if idx <= len(hero[12]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[12][idx]}")
        if hero[12][idx] == "зелье":
            hero[2] += 10
            if hero[2] > hero[1]:
                hero[2] = hero[1]
        elif hero[12][idx] == "зелье опыта":
            hero[4] += 800
        elif hero[12][idx] == "яблоко":
            pass
        else:
            print("употребилчто то не известное")
        hero[12].pop(idx)
    else:
        print("нет такого")


def play_dise(hero: list, bet: str) -> None:
    try:
        bet = int(bet)

    except ValueError:
        print("Ставка должна быть числом")

    else:
        if bet > 0:
            if hero[11] >= bet:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"{hero[0]} выбросил {hero_score}")
                print(f"Трактирщик выбросил {casino_score}")
                if hero_score > casino_score:
                    hero[11] += bet
                    print(f"{hero[0]} выйграл и забирает {bet} монет")
                elif hero_score < casino_score:
                    hero[11] -= bet
                    print(f"{hero[0]} проиграл {bet} монет")
                else:
                    print("ничья")
            else:
                print(f"У {hero[0]} нет столько монет")
        else:
            print("такая ставка невозможна, минимальная ставка начинается от 1 монеты")

        input("\n Нажмите ENTER чтобы продолжить")

def start_fight(hero: list) -> None:
    """
    TODO:
    нужен противник
    обмен ударами пока игрок и противник живы
    итог боя: проигрыш или победа
    победа: добавить опыт от врага, забрать предметы от врага в инвентарь героя
    проигрыш: закончить игру
    """,
    enemy = make_hero(name="Гладиатор",xp_now=30,money=100, inventary=["Меч гладиатора"])
    while hero[2] > 0 and enemy[2] > 0:
        os.system("cls")
        combat_turn(hero, enemy)
        combat_turn(enemy, hero)
        print("")
        show_hero(hero)
        show_hero(enemy)
        pause = input("Чтобы продолжить нажмите ENTER")
    combat_result(hero, enemy)


def combat_result(hero, enemy) -> None:
    """
    Результат боя:
        если победил игрок:
            забирает опыт, деньги, предметы инвентаря


    """
    if hero[2] > 0 and enemy[2] <= 0:
        print(f"{hero[0]} победил противника {enemy[0]} и в награду получает: ")
        hero[5] += enemy[5]
        print(enemy[5], "опыта")
        hero[10] += enemy[10]
        print(enemy[10], "монет")
        print("И забирает предметы:")
        for item in enemy[12]:
            print(item, end=",")
        print
        hero[12] += enemy[12]
        levelup(hero)
        """
        [5] xp_now - текущий опыт
        [11] money - деньги
        [12] inventary - инвентарь список
        """
    elif enemy[2] > 0 and hero[2] <= 0:
        print(f"{enemy[0]} победил противника {hero[0]}")
        print("Игра должна закончится тут")
    else:
        print("Ничья")

def combat_turn(attacker: list, defender: list) -> None:
    """TODO: DND?"""
    if attacker[2] > 0:
        damage = attacker[6]
        defender[2] -= damage
        print(f"{attacker[0]} ударил {defender[0]} на {damage} здоровья")



def choose_option(hero: list, text: str, options: list) -> int:
    os.system("cls")
    show_hero(hero)
    print(text)
    for num, option in enumerate(options):
        print(f"{num}. {option}")
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:  # выполнится если трай не получится
        print("Ввод должен быть целым неотрицательным числом")
    else: # если трай удался
        if option < len(options) and option > -1:
            return option
        else:
            print("Нет такого выбора")


def visit_hub(hero) -> None:
    text = f"{hero[0]} приехал в Хаб.Здесь есть чем заняться:"
    options = [
        "Заглянуть в лавку алхимика",
        "Заглянуть в оружейный",
        "Поехать в казино",
        "Выйти в главное меню"
    ]
    option = choose_option(hero, text, options)
    os.system("cls")
    if option == 0:
        return visit_shop(hero)
    elif option == 1:
        return visit_armory(hero)
    elif option == 1:
        return visit_casino(hero)
    elif option == 2:
        print("Типа, ушел в меню")
    input("\n Нажмите ENTER чтобы продолжить от хаба")


def visit_shop(hero: list) -> None:
    text = f"{hero[0]} приехал в в лавку алхимика.Здесь пахнет итальянскими травами и что то продается:"
    options = [
            "Купить зелье лечения за 10 монет",
            "купить зелье опыта за 30 монет",
            "Уйти из лавки в Хаб"
    ]
    option = choose_option(hero, text, options)
    if option == 0:
        buy_item(hero, "зелье лечения", 10)
        return visit_shop(hero)
    elif option == 1:
        buy_item(hero,"зелье опыта", 30)
        return visit_shop(hero)
    elif option == 2:
        return visit_hub(hero)


def visit_armory(hero: list) -> None:
    text = f"{hero[0]} приехал в оружейный.Здесь пахнет железом и что то продается:"
    options = [
        "Купить меч варвара за 100 монет",
        "купить щит крестоносца за 60 монет",
        "Уйти из оружейного в Хаб"
    ]
    option = choose_option(hero, text, options)
    if option == 0:
        buy_item(hero, "меч варвара", 100)
        return visit_armory(hero)
    elif option == 1:
        buy_item(hero, "щит крестоносца", 60)
        return visit_armory(hero)
    elif option == 2:
        return visit_hub(hero)

def visit_casino(hero: list) -> None:
    text = f"{hero[0]} приехал в казино.Здесь пахнет деньгами и есть чем заняться:"
    options = [
        "Сыграть в кости",
        "Уйти из казино в Хаб"
    ]
    option = choose_option(hero, text, options)
    if option == 0:
        bet = input("Выберете ставку: ")
        return play_dise(hero, bet)
    elif option == 1:
        return visit_hub(hero)


def visit_arena(hero):
    pass
