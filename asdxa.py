from random import choice, randint


first_name = ("Жран","Дрын", "Жлыг")
last_name = ("Кривой", "Злопаметный", "Дикий")



def make_hero(
        name=None,
        hp_max=None,
        hp_now=None,
        lvl=1,
        xp_next=1000,
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
        hp_max = hp_now

    if not hp_now:
        hp_now = randint(1, 100)

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

    return [name,
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

p1 = make_hero()
p2 = make_hero()
p3 = make_hero()


def show_hero(hero):
    pass



    p1 = make_hero()
    p2 = make_hero()
    p3 = make_hero()
