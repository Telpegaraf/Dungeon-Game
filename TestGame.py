import random
import pickle
import os


class Character():

    def __init__(self, health, damage, evasion, persuation, precision,
                 fullInventory, trinket, coins, count, unique, bonus):
        self.health = health
        self.damage = damage
        self.evasion = evasion
        self.persuation = persuation
        self.precision = precision
        self.fullInventory = fullInventory
        self.trinket = trinket
        self.coins = coins
        self.count = count
        self.unique = unique
        self.bonus = bonus


class TraderItems():
    traderinventory1 = ''
    traderinventory2 = ''
    traderinventory3 = ''


fighter = Character(random.randint(22, 28), random.randint(8, 12), random.randint(24, 36), random.randint(16, 24),
                    random.randint(24, 36), '', 0, 0, 0, 'Зелье здоровья', 2)
rouge = Character(random.randint(18, 22), random.randint(6, 10), random.randint(36, 48), random.randint(16, 24),
                  random.randint(36, 48), '', 0, 0, 0, 'Дымовая шашка', 3)
bard = Character(random.randint(14, 18), random.randint(4, 8), random.randint(24, 36), random.randint(36, 48),
                 random.randint(24, 36), '', 0, 0, 0, 'Диковинка на обмен', 4)


class Dialogs:
    @staticmethod
    def choose_a_class():
        os.system('cls')
        print('Выберите ваш класс:\n1)Воин\n2)Плут\n3)Бард')

    def menu_dialogs():
        print('Выберите действие: \n1) Идти вглубь подземелья\n2) Посмотреть инвентарь\n3) Посмотреть свои параметры')


def choose_class():
    Dialogs.choose_a_class()

    player_class = input()

    if player_class == '1':
        player = fighter
    elif player_class == '2':
        player = rouge
    elif player_class == '3':
        player = bard
    else:
        print('')
        choose_class()
    os.system('cls')
    player.fullHealth = player.health
    menu(player)


monstersFromFirstLevel = [
    {'Monsters': 'Гигантский Паук', 'Damage': 6, 'Health': 4, 'Dodge': 16, 'Resistance': 8, 'Precision': 10,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Рой крыс', 'Damage': 4, 'Health': 8, 'Dodge': 8, 'Resistance': 18, 'Precision': 12,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Ядовитая змея', 'Damage': 6, 'Health': 6, 'Dodge': 12, 'Resistance': 12, 'Precision': 12,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Тень', 'Damage': 6, 'Health': 8, 'Dodge': 16, 'Resistance': 16, 'Precision': 16,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Скелет', 'Damage': 8, 'Health': 10, 'Dodge': 28, 'Resistance': 20, 'Precision': 8,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Гоблин', 'Damage': 8, 'Health': 10, 'Dodge': 24, 'Resistance': 24, 'Precision': 8,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Разбойник', 'Damage': 8, 'Health': 12, 'Dodge': 24, 'Resistance': 24, 'Precision': 12,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Неповоротливый зомби', 'Damage': 10, 'Health': 14, 'Dodge': 20, 'Resistance': 24, 'Precision': 8,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Живая слизь', 'Damage': 10, 'Health': 20, 'Dodge': 32, 'Resistance': 40, 'Precision': 12,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Вампир', 'Damage': 10, 'Health': 16, 'Dodge': 32, 'Resistance': 40, 'Precision': 20,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Призрак', 'Damage': 11, 'Health': 16, 'Dodge': 40, 'Resistance': 32, 'Precision': 28,
     'coins': random.randint(1, 3)},
    {'Monsters': 'Каменный голем', 'Damage': 12, 'Health': 15, 'Dodge': 32, 'Resistance': 40, 'Precision': 12,
     'coins': random.randint(1, 3)},
]

monstersFromSecondLevel = [
    {'Monsters': 'Чумной волк', 'Damage': 13, 'Health': 12, 'Dodge': 36, 'Resistance': 18, 'Precision': 54,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Дикий медведь', 'Damage': 14, 'Health': 16, 'Dodge': 12, 'Resistance': 36, 'Precision': 18,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Гигантская змея', 'Damage': 10, 'Health': 9, 'Dodge': 12, 'Resistance': 18, 'Precision': 36,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Спектр', 'Damage': 13, 'Health': 18, 'Dodge': 48, 'Resistance': 48, 'Precision': 24,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Скелет-лучник', 'Damage': 15, 'Health': 6, 'Dodge': 36, 'Resistance': 48, 'Precision': 36,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Хобгоблин', 'Damage': 17, 'Health': 15, 'Dodge': 36, 'Resistance': 18, 'Precision': 36,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Командир разбойников', 'Damage': 16, 'Health': 18, 'Dodge': 18, 'Resistance': 18, 'Precision': 36,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Резвый зомби', 'Damage': 11, 'Health': 21, 'Dodge': 36, 'Resistance': 72, 'Precision': 72,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Студенистый куб', 'Damage': 12, 'Health': 30, 'Dodge': 18, 'Resistance': 72, 'Precision': 24,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Лорд Вампир', 'Damage': 19, 'Health': 21, 'Dodge': 36, 'Resistance': 36, 'Precision': 48,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Банши', 'Damage': 19, 'Health': 18, 'Dodge': 48, 'Resistance': 24, 'Precision': 48,
     'coins': random.randint(4, 6)},
    {'Monsters': 'Железный голем', 'Damage': 19, 'Health': 24, 'Dodge': 12, 'Resistance': 24, 'Precision': 36,
     'coins': random.randint(4, 6)},
]

monstersFromThirdLevel = [
    {'Monsters': 'Василиск', 'Damage': 19, 'Health': 18, 'Dodge': 48, 'Resistance': 24, 'Precision': 48,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Химера', 'Damage': 18, 'Health': 27, 'Dodge': 24, 'Resistance': 48, 'Precision': 48,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Мимик', 'Damage': 12, 'Health': 12, 'Dodge': 72, 'Resistance': 72, 'Precision': 48,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Ожившая статуя', 'Damage': 22, 'Health': 24, 'Dodge': 48, 'Resistance': 48, 'Precision': 48,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Скелет минотавра', 'Damage': 18, 'Health': 18, 'Dodge': 72, 'Resistance': 96, 'Precision': 48,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Минотавр', 'Damage': 19, 'Health': 18, 'Dodge': 48, 'Resistance': 36, 'Precision': 60,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Рыцарь смерти', 'Damage': 22, 'Health': 24, 'Dodge': 48, 'Resistance': 36, 'Precision': 72,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Тролль', 'Damage': 22, 'Health': 30, 'Dodge': 36, 'Resistance': 36, 'Precision': 60,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Бехолдер', 'Damage': 27, 'Health': 24, 'Dodge': 48, 'Resistance': 144, 'Precision': 60,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Адская гончая', 'Damage': 29, 'Health': 24, 'Dodge': 72, 'Resistance': 72, 'Precision': 72,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Безумный ученый', 'Damage': 27, 'Health': 24, 'Dodge': 60, 'Resistance': 108, 'Precision': 72,
     'coins': random.randint(7, 9)},
    {'Monsters': 'Стальной голем', 'Damage': 30, 'Health': 45, 'Dodge': 36, 'Resistance': 36, 'Precision': 36,
     'coins': random.randint(7, 9)},
]

finalBoss = [
    {'Monsters': 'Древний Дракон', 'Damage': 32, 'Health': 48, 'Dodge': 144, 'Resistance': 288, 'Precision': 144,
     'coins': random.randint(150, 300)},
    {'Monsters': 'Бафомет', 'Damage': 38, 'Health': 36, 'Dodge': 144, 'Resistance': 144, 'Precision': 288,
     'coins': random.randint(150, 300)},
    {'Monsters': 'Адамантиновый Колосс', 'Damage': 35, 'Health': 40, 'Dodge': 288, 'Resistance': 144, 'Precision': 144,
     'coins': random.randint(150, 300)},
]

inventoryFromTraderFirstLevel = [
    {'items': 'Ложка удачи', 'Damage': 0, 'Health': 0, 'Evasion': 48, 'Persuation': 0, 'Precision': 48,
     'price': random.randint(3, 9)},
    {'items': 'Кольцо победы', 'Damage': 2, 'Health': 8, 'Evasion': 0, 'Persuation': 48, 'Precision': 0,
     'price': random.randint(6, 9)},
    {'items': 'Кожаный доспех', 'Damage': 0, 'Health': 8, 'Evasion': 36, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(9, 15)},
    {'items': 'Сфера Ничего', 'Damage': 0, 'Health': 0, 'Evasion': 0, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(15, 15)},
    {'items': 'Деревянный щит', 'Damage': 0, 'Health': 8, 'Evasion': 48, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(9, 12)},
    {'items': 'Серьга очарования', 'Damage': 0, 'Health': 0, 'Evasion': 24, 'Persuation': 48, 'Precision': 0,
     'price': random.randint(6, 9)},
    {'items': 'Простой меч', 'Damage': 10, 'Health': 0, 'Evasion': 0, 'Persuation': 0, 'Precision': 48,
     'price': random.randint(9, 15)},
    {'items': 'Мантия переговорщика', 'Damage': 0, 'Health': 0, 'Evasion': 0, 'Persuation': 64, 'Precision': 0,
     'price': random.randint(6, 9)},
    {'items': 'Укрепленные сапоги', 'Damage': 2, 'Health': 12, 'Evasion': 24, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(9, 12)},
]

inventoryFromTraderSecondLevel = [
    {'items': 'Стальные наручи', 'Damage': 6, 'Health': 18, 'Evasion': 72, 'Persuation': 0, 'Precision': 12,
     'price': random.randint(18, 27)},
    {'items': 'Шарф обаяния', 'Damage': 0, 'Health': 0, 'Evasion': 48, 'Persuation': 72, 'Precision': 0,
     'price': random.randint(15, 21)},
    {'items': 'Кожаный доспех', 'Damage': 0, 'Health': 8, 'Evasion': 36, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(9, 15)},
    {'items': 'Сфера Ничего', 'Damage': 0, 'Health': 0, 'Evasion': 0, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(15, 15)},
    {'items': 'Деревянный щит', 'Damage': 0, 'Health': 8, 'Evasion': 48, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(9, 12)},
    {'items': 'Зачарованный колчан', 'Damage': 8, 'Health': 0, 'Evasion': 12, 'Persuation': 0, 'Precision': 72,
     'price': random.randint(21, 24)},
    {'items': 'Простой меч', 'Damage': 10, 'Health': 0, 'Evasion': 0, 'Persuation': 0, 'Precision': 48,
     'price': random.randint(9, 15)},
    {'items': 'Брошь защиты', 'Damage': 0, 'Health': 18, 'Evasion': 72, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(21, 24)},
    {'items': 'Укрепленные сапоги', 'Damage': 2, 'Health': 12, 'Evasion': 24, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(9, 12)},
]

inventoryFromTraderThirdLevel = [
    {'items': 'Стальные наручи', 'Damage': 8, 'Health': 18, 'Evasion': 72, 'Persuation': 0, 'Precision': 12,
     'price': random.randint(18, 27)},
    {'items': 'Кулон мастерства', 'Damage': 12, 'Health': 12, 'Evasion': 48, 'Persuation': 48, 'Precision': 48,
     'price': random.randint(24, 36)},
    {'items': 'Мифриловый меч', 'Damage': 20, 'Health': 0, 'Evasion': 24, 'Persuation': 0, 'Precision': 48,
     'price': random.randint(36, 45)},
    {'items': 'Сфера Ничего', 'Damage': 0, 'Health': 0, 'Evasion': 0, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(15, 15)},
    {'items': 'Адамантиновый доспех', 'Damage': 0, 'Health': 24, 'Evasion': 72, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(30, 42)},
    {'items': 'Зачарованный колчан', 'Damage': 6, 'Health': 0, 'Evasion': 12, 'Persuation': 0, 'Precision': 72,
     'price': random.randint(21, 24)},
    {'items': 'Королевский парфюм', 'Damage': 0, 'Health': 0, 'Evasion': 0, 'Persuation': 144, 'Precision': 0,
     'price': random.randint(27, 33)},
    {'items': 'Брошь защиты', 'Damage': 0, 'Health': 18, 'Evasion': 72, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(21, 24)},
    {'items': 'Плащ ускользания', 'Damage': 0, 'Health': 0, 'Evasion': 144, 'Persuation': 0, 'Precision': 0,
     'price': random.randint(30, 36)},
]

helpinfo = [
    'Совет № 1/5: Если у монстра осталось меньше 50% здоровья, то убедить его не сражаться становится в 2 раза проще.',
    'Совет № 2/5: Безделушки существуют не просто так, они позволяют лучше понимать монстров и их мотивы, но безделушки полезны лишь только в большом количестве.',
    'Совет № 3/5: Вы не сможете встретить больше 3 торговцев и трёх мест отдыха за одно подземелье, поэтому рассчитывайте свои силы и ваш план заранее.',
    'Совет № 4/5: Существует лишь один шанс из четырёх, что вам удастся сбежать от монстра. В остальных случаях он попробует вас ударить.',
    'Совет № 5/5: Не все подсказки одинаково ценные. Это самая бесполезная.']


def random_array_element(array: list[str]):
    i = random.randint(0, len(array) - 1)
    return array[i]


print(
    'Вы искатель сокровищ и вам удалось обнаружить вход в подземелье, которое раньше считалось затерянным. Что будете делать дальше?' + '\n')


def menu(player):
    while True:
        if player.count <= 31:
            Dialogs.menu_dialogs()
            if player.trinket >= 10:
                print('4) Собрать мозайку из 10 безделушек')
            if player.trinket >= 20:
                print('5) Собрать большую мозайку из 20 безделушек')
            if player.unique == 'Зелье здоровья' and player.bonus > 0:
                print('4) Выпить зелье здоровья')
            n = input()

            if n == '1':
                menu_encounter(player)
            if n == '2':
                menu_inventory(player)
            if n == '3':
                menu_stats(player)
            if n == '4' and player.trinket >= 10:
                player.trinket -= 10
                trinket_buff(player)
            if n == '5' and player.trinket >= 20:
                player.trinket -= 20
                trinket_buff(player)
            if n == '4' and player.bonus > 0 and player.unique == 'Зелье здоровья':
                player.bonus -= 1
                lasthealth = player.health
                player.health = min(player.health + int((player.fullHealth / 2)), player.fullHealth)
                print('Вы восстановили здоровье в размере: ' + str(
                    (player.health - lasthealth)) + '. Теперь ваше здоровье: ' + str(player.health))
            else:
                print()
        else:
            print('Вам удалось добыть сокровище, которое поможет вам достичь всего того, о чем вы мечтали, ведь это:')
            print('Кольцо Трёх Желаний')
            print('Поздравляем! Вы победили всех врагов и прошли игру!')
            input()
            exit()


def menu_stats(player):
    os.system('cls')
    print("\n" + "Параметры игрока:" + "\n")

    print("Здоровье: " + str(player.health) + ' из ' + str(player.fullHealth))
    print("Урон: " + str(player.damage))
    print("Уклонение: " + str(player.evasion))
    print("Убеждение: " + str(player.persuation))
    print("Точность: " + str(player.precision))
    print()


firstlist = list(range(5, 11))
secondlist = list(range(14, 21))
thirdlist = list(range(24, 31))

random.shuffle(firstlist)
random.shuffle(secondlist)
random.shuffle(thirdlist)
finallist = list(range(0, 5)) + firstlist + list(range(11, 14)) + secondlist + list(range(21, 24)) + thirdlist + list(
    range(31, 31))


def menu_inventory(player):
    os.system('cls')
    print('Количество монет: ' + str(player.coins))
    print('Безделушки монстров: ' + str(player.trinket))
    print(f"{player.unique}: {player.bonus}")
    print("\n" + 'Инвентарь игрока:' + player.fullInventory + '\n')


def menu_encounter(player):
    if finallist[player.count] == 7 or finallist[player.count] == 17 or finallist[player.count] == 27:
        itemtraders(player)
    if finallist[player.count] == 5 or finallist[player.count] == 15 or finallist[player.count] == 25:
        rest(player)
    else:
        battle(player)


def vendor_trade(player):
    while True:
        print('Ваше количество монет: ' + str(player.coins) + '\n')
        priceitem1 = TraderItems.traderinventory1['price']
        priceitem2 = TraderItems.traderinventory2['price']
        priceitem3 = TraderItems.traderinventory3['price']
        print('1) Купить ' + TraderItems.traderinventory1['items'] + ', потратив количество монет: ' + str(
            priceitem1) + '?')
        print('2) Купить ' + TraderItems.traderinventory2['items'] + ', потратив количество монет: ' + str(
            priceitem2) + '?')
        print('3) Купить ' + TraderItems.traderinventory3['items'] + ', потратив количество монет: ' + str(
            priceitem3) + '?')
        print('4) Пройти мимо')
        trader = input()
        if trader == '1' and player.coins >= TraderItems.traderinventory1['price']:
            item = TraderItems.traderinventory1
        elif trader == '1' and player.coins < TraderItems.traderinventory1['price']:
            print('\n' + 'Недостаточно монет! Сделка не состоится.')
            vendor_trade(player)
        elif trader == '2' and player.coins >= TraderItems.traderinventory2['price']:
            item = TraderItems.traderinventory2
        elif trader == '2' and player.coins < TraderItems.traderinventory2['price']:
            print('\n' + 'Недостаточно монет! Сделка не состоится.')
            vendor_trade(player)
        elif trader == '3' and player.coins >= TraderItems.traderinventory3['price']:
            item = TraderItems.traderinventory3
        elif trader == '3' and player.coins < TraderItems.traderinventory3['price']:
            print('\n' + 'Недостаточно монет! Сделка не состоится.')
            vendor_trade(player)
        elif trader == '4':
            player.count += 1
            os.system('cls')
            menu(player)
        else:
            print()
            vendor_trade(player)

        items = item['items']
        player.damage = item['Damage'] + player.damage
        player.health = item['Health'] + player.health
        player.fullHealth = item['Health'] + player.fullHealth
        player.evasion = item['Evasion'] + player.evasion
        player.persuation = item['Persuation'] + player.persuation
        player.precision = item['Precision'] + player.precision
        player.coins = player.coins - item['price']
        player.count += 1
        player.fullInventory = player.fullInventory + '\n' + items
        print(
            'Вы приобрели ' + items + '. Теперь вы знаете характеристики этого предмета:' 'Ваше количество монет: ' + str(
                player.coins) + ".")
        print('\n' + 'Урон: ' + str(item['Damage']) + '\n' + 'Здоровье: ' + str(
            item['Health']) + '\n' + 'Уклонение: ' + str(item['Evasion']))
        print('Убеждение: ' + str(item['Persuation']) + '\n' + 'Точность: ' + str(
            item['Precision']))
        print('\n' + 'Ваше количество монет: ' + str(player.coins) + "." + '\n')
        menu(player)


def rest(player):
    os.system('cls')
    floor = player.count + 1
    print(f"Вы спускаетесь на {floor} этаж")
    print('***********')
    while True:
        print('Вы находите неплохое место для отдыха. Желаете отдохнуть или улучшить свои боевые навыки?')
        print(
            '1) Отдохнуть и восстановить силы. Ваше здоровье: ' + str(player.health) + ' из ' + str(player.fullHealth))
        print('2) Прокачать навык')
        longrest = input()

        if longrest == '1':
            lasthealth = player.health
            player.health = min(player.health + int((player.fullHealth / 2)), player.fullHealth)
            print('Вы восстановили здоровье в размере: ' + str(
                (player.health - lasthealth)) + '. Теперь ваше здоровье: ' + str(player.health))
            rest_effects(player)
        elif longrest == '2':
            print('Вы решаете прокачать один из навыков. Но какой именно?')
            healthrest = random.randint(8, 12)
            damagerest = random.randint(8, 12)
            evasionrest = random.randint(24, 36)
            persuationrest = random.randint(16, 24)
            precisionrest = random.randint(24, 36)
            print('1) Увеличить здоровье на ' + str(healthrest))
            print('2) Увеличить урон на ' + str(damagerest))
            print('3) Увеличить уклонение на ' + str(evasionrest))
            print('4) Увеличить убеждение на ' + str(persuationrest))
            print('5) Увеличить точность на ' + str(precisionrest))
            while True:
                chooseskill = input()
                if chooseskill == '1':
                    player.health += healthrest
                    player.fullHealth += healthrest
                    rest_effects(player)
                if chooseskill == '2':
                    player.damage += damagerest
                    rest_effects(player)
                if chooseskill == '3':
                    player.evasion += evasionrest
                    rest_effects(player)
                if chooseskill == '4':
                    player.persuation += persuationrest
                    rest_effects(player)
                if chooseskill == '5':
                    player.precision += precisionrest
                    rest_effects(player)
                else:
                    os.system('cls')
                    print()
        else:
            print()


def rest_effects(player):
    print('***********')
    print(random.choice(helpinfo))
    player.count += 1
    input()
    menu(player)


def battle(player):
    os.system('cls')
    floor = player.count + 1
    print(f"Вы спускаетесь на {floor} этаж")
    print('***********')
    if player.count <= 10:
        encountermonster = random.choice(monstersFromFirstLevel)
    elif player.count <= 20:
        encountermonster = random.choice(monstersFromSecondLevel)
    elif player.count < 30:
        encountermonster = random.choice(monstersFromThirdLevel)
    elif player.count == 30:
        encountermonster = random.choice(finalBoss)
        print(
            'Вы добрались до последнего зала этого древнего подземелья. Главное сокровище уже близко, но его охраняет Древний страж: ' +
            encountermonster['Monsters'])
        input()

    battlemonster = encountermonster['Monsters']
    damagemonster = encountermonster['Damage']
    healthmonster = encountermonster['Health']
    negotiationmonster = healthmonster / 2
    dodgemonster = encountermonster['Dodge']
    resistancemonster = encountermonster['Resistance']
    coinsmonster = encountermonster['coins']
    precisionmonster = encountermonster['Precision']

    while True:

        print('Вас атакует ' + battlemonster)
        print('Ваши действия?')
        print('1) Атаковать монстра')
        print('2) Попробовать сбежать')
        print('3) Убедить монстра не сражаться с вами')
        if player.unique == 'Дымовая шашка' and player.bonus > 0:
            print('4) Сбежать с помощью дымовой шашки')
        if player.unique == 'Диковинка на обмен' and player.bonus > 0 and player.count != 30:
            print('4) Подарить монстру диковинку')
        choosebattle = input()

        if choosebattle == '1':
            attackplayer = random.randint(0, player.precision) + random.randint(0, player.precision)
            defencemonster = random.randint(0, dodgemonster) + random.randint(0, dodgemonster)
            attackmonster = random.randint(0, precisionmonster) + random.randint(0, precisionmonster)
            defenceplayer = random.randint(0, player.evasion) + random.randint(0, player.evasion)
            if attackplayer > defencemonster:
                damagetomonster = max(random.randint(0, player.damage) + random.randint(0, player.damage), 1)
                healthmonster -= damagetomonster
                print('Вы наносите по монстру урон: ' + str(damagetomonster))
                print('Здоровье монстра: ' + max(str(healthmonster), str(0)))
                if healthmonster <= 0:
                    player.count += 1
                    player.coins += coinsmonster
                    print(battlemonster + ' погибает. Вы получаете количество монет: ' + str(coinsmonster) + '\n')
                    menu(player)
                else:
                    if attackmonster > defenceplayer:
                        player.health -= damagemonster
                        print(battlemonster + ' наносит по вам урон: ' + str(damagemonster))
                        print('Ваше здоровье: ' + str(player.health))
                        if player.health <= 0:
                            print(
                                'Вы погибаете, так и не добравшись до главного сокровища этих подземелий...' + '\n' + 'Кто знает, может следующему искателю приключений повезёт больше?')
                            input()
                            exit()
                    else:
                        print('Вы успешно уклоняетесь от атаки монстра!')
            else:
                print('Вы промахиваетесь!')
                if attackmonster > defenceplayer:
                    player.health -= damagemonster
                    print('Монстр наносит по вам урон: ' + str(damagemonster))
                    print('Ваше здоровье: ' + str(player.health))
                    if player.health <= 0:
                        print(
                            'Вы погибаете, так и не добравшись до главного сокровища этих подземелий...' + '\n' + 'Кто знает, может следующему искателю приключений повезёт больше?')
                        input()
                        exit()
                else:
                    print('Вы успешно уклоняетесь от атаки монстра!')
        if choosebattle == '2':
            if random.random() < 0.25:
                player.count += 1
                print('Вам удается сбежать от монстра!')
                input()
                menu(player)
            else:
                print('Вам не удается сбежать и теперь ' + battlemonster + ' вас атакует.')
                player.health -= damagemonster
                print(battlemonster + ' наносит по вам урон: ' + str(damagemonster))
                print('Ваше здоровье: ' + str(player.health))
                if player.health <= 0:
                    print(
                        'Вы погибаете, так и не добравшись до главного сокровища этих подземелий...' + '\n' + 'Кто знает, может следующему искателю приключений повезёт больше?')
                    input()
                    exit()
        if choosebattle == '3':
            if healthmonster > negotiationmonster:
                negotiationplayer = random.randint(0, player.persuation) + random.randint(0, player.persuation)
                willmonster = random.randint(0, resistancemonster) + random.randint(0, resistancemonster)
                if negotiationplayer > willmonster:
                    player.count += 1
                    player.trinket += 1
                    print(
                        'Вам удается убедить монстра не сражаться с вами. В благодарность ' + battlemonster + ' дарит вам какую то безделушку.' + '\n')
                    menu(player)
                else:
                    attackmonster = random.randint(0, precisionmonster) + random.randint(0, precisionmonster)
                    defenceplayer = random.randint(0, player.evasion) + random.randint(0, player.evasion)
                    if attackmonster > defenceplayer:
                        player.health -= damagemonster
                        print('Вам не удалось убедить монстра и теперь он вас атакует!')
                        print('Монстр наносит по вам урон: ' + str(damagemonster))
                        print('Ваше здоровье: ' + str(player.health))
                        if player.health <= 0:
                            print(
                                'Вы погибаете, так и не добравшись до главного сокровища этих подземелий...' + '\n' + 'Кто знает, может следующему искателю приключений повезёт больше?')
                            input()
                            exit()
                    else:
                        print('Вам не удалось убедить монстра и теперь он вас атакует!')
                        print('Вы успешно уклоняетесь от атаки монстра!')
            else:
                negotiationplayer = random.randint(0, player.persuation) + random.randint(0, player.persuation)
                willmonster = random.randint(0, resistancemonster)
                if negotiationplayer > willmonster:
                    player.count += 1
                    player.trinket += 1
                    print(
                        'Вам удается убедить монстра не сражаться с вами. В благодарность ' + battlemonster + ' дарит вам какую то безделушку.' + '\n')
                    menu(player)
                else:
                    attackmonster = random.randint(0, precisionmonster) + random.randint(0, precisionmonster)
                    defenceplayer = random.randint(0, player.evasion) + random.randint(0, player.evasion)
                    if attackmonster > defenceplayer:
                        player.health -= damagemonster
                        print('Вам не удалось убедить монстра и теперь он вас атакует!')
                        print(battlemonster + ' наносит по вам урон: ' + str(damagemonster))
                    else:
                        print('Вам не удалось убедить монстра и теперь он вас атакует!')
                        print('Вы успешно уклоняетесь от атаки монстра!')
        if choosebattle == '4' and player.unique == 'Дымовая шашка':
            print('Вы используете дымовую шашку, чтобы избежать встречи с монстром и успешно продвигаетесь дальше')
            player.count += 1
            player.bonus -= 1
            input()
            menu(player)
        if choosebattle == '4' and player.unique == 'Диковинка на обмен' and player.count != 30:
            print(
                'Вы дарите монстру диковинку и он не только больше не хочет с вами сражаться, но ещё и дарит вам немного золотых монет: ' + str(
                    coinsmonster))
            player.count += 1
            player.bonus -= 1
            player.coins += coinsmonster
            input()
            menu(player)


        else:
            print()


def trinket_buff(player):
    if player.trinket < 20:
        print('Вы собираете мозайку из 10 безделушек, которые образуют единый текст и вам наконец'
              ' удается расшифровать его. Теперь вы лучше понимаете язык монстров.')
        buff = random.randint(48, 96)
    else:
        print('Вы собираете мозайку из 10 безделушек, которые образуют единый текст и вам наконец'
              ' удается расшифровать его. Теперь вы лучше понимаете язык монстров.')
        buff = random.randint(96, 168)
    player.persuation += buff
    print('Ваш навык убеждения теперь: ' + str(player.persuation))
    player.fullInventory = player.fullInventory + '\n' + 'Мозайка монстров'
    menu(player)


def itemtraders(player):
    os.system('cls')
    floor = player.count + 1
    print(f"Вы спускаетесь на {floor} этаж")
    print('***********')
    print('Вы встретили загадочного торговца в подземелье. Желаете осмотреть его товары или пройдёте мимо?')
    random.shuffle(inventoryFromTraderFirstLevel)
    random.shuffle(inventoryFromTraderSecondLevel)
    random.shuffle(inventoryFromTraderThirdLevel)
    if player.count <= 10:
        TraderItems.traderinventory1 = inventoryFromTraderFirstLevel[0]
        TraderItems.traderinventory2 = inventoryFromTraderFirstLevel[1]
        TraderItems.traderinventory3 = inventoryFromTraderFirstLevel[2]
    elif player.count <= 20:
        TraderItems.traderinventory1 = inventoryFromTraderSecondLevel[0]
        TraderItems.traderinventory2 = inventoryFromTraderSecondLevel[1]
        TraderItems.traderinventory3 = inventoryFromTraderSecondLevel[2]
    elif player.count <= 30:
        TraderItems.traderinventory1 = inventoryFromTraderThirdLevel[0]
        TraderItems.traderinventory2 = inventoryFromTraderThirdLevel[1]
        TraderItems.traderinventory3 = inventoryFromTraderThirdLevel[2]
    vendor_trade(player)


choose_class()
