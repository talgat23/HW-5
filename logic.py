import random
from decouple import config

MY_MONEY = int(config('MY_MONEY'))


def start_game():
    lst = range(1, 31)
    slot = random.choice(lst)
    user_input = int(input('Введите сумму ставки'))
    bet = int(input("Ведите слот"))

    if slot == bet:
        MY_MONEY + user_input * 2
        print(f'Вы выиграли {user_input * 2}')
    else:
        MY_MONEY - user_input
        print(f'Вы проиграли {user_input} сумму')
