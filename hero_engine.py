from random import randint, choice

first_name = ("Жран","Дрын","Брысь","Жлыг")
last_names = ("Зловонный","Борзый","Дикий","Ужасный")


def make_hero(
    name = None,
    hp = None,
    xp = None,
    attack = None,
    defence = None,
    money = None,
    potions = None,
) -> tuple:
    if not name:
        name = f"{choice(first_name)} {choice(last_names)}"
    if not hp:
        hp = randint(1, 100)
    if not xp:
        xp = randint(1, 10)
    if not attack:
        attack = randint(1, 10)
    if not defence:
        defence = randint(1, 100)
    if not money:
        money = randint(0, 500)
    if not potions:
        potions = randint(0, 2)


    return (name, hp, attack, defence, money, potions)

player = make_hero(name="Вася Питонов", hp=100, xp=50, potions=1, defence=1, money=5, attack=5)
enemy_0 = make_hero()
enemy_1 = make_hero()
enemy_2 = make_hero()
print(player)
print(enemy_0)
print(enemy_1)
print(enemy_2)


