import os
import pickle

from duplicity.config import action

from class_man import Man
import glob
from constants import TirednessParameters

ACTIONS_MENU = {
    "self": "print",
    "eat": "eat",
    "shopping": "shopping",
    "work": "work",
    "gym": "gym",
    "study": "study",
    "sleep": "sleep",
    "heal": "heal",
    "fight": "fight",
    "cook": "cook",
    "invest": "invest",
    "casino": "casino",
    "date" : "date",
    "meditate" : "meditate",
    'read' : 'read',
}

commands = ("Возможные действия:\n"
            "self - информация о себе         eat - поесть\n"
            "cook - приготовить еды           shopping - купить еды\n"
            "work - пойти работать            gym - пойти в качалку\n"
            "study - пойти на учёбу           fight - участвовать в бою\n"
            "sleep - пойти спать              heal - полечиться у врача\n"
            "menu - открыть меню              invest - инвестировать\n"
            "help - список действий           casino - пойти в казино\n"
            "date - сходить на свидание       meditate - помедитировать\n"
            "read - почитать книгу")

tiredness_list = [
    "gym",
    "work",
    "study",
    "casino",
    "date",
]


def save(man, file_name):
    with open(f'{file_name}.pkl', 'wb') as f:
        pickle.dump(man, f)


def load(file_name):
    with open(f'{file_name}.pkl', 'rb') as f:
        return pickle.load(f)


while True:
    saves = glob.glob('*.pkl')
    if len(saves) == 0:
        character_name = input('Введите имя персонажа: ')
        print(f"Добро пожаловать, {character_name}")
        man = Man(character_name)
        print(commands)
        break
    else:
        played = input("новая игра или загрузить(Введите n или l):\n")
        if played == 'n':
            character_name = input('Введите имя персонажа: ')
            print(f"Добро пожаловать, {character_name}")
            man = Man(character_name)
            print(commands)
            break
        elif played == 'l':
            print(glob.glob('*.pkl'))
            file_name = input("Введите название сохранения до точки ")
            man = load(file_name)
            character_name = man.name
            print(commands)
            break
        else:
            print(f'неизвестное действие - {played}')

action = ""
menu_action = ""
while True:
    if getattr(man, 'alive') and action == "sleep":
        print(f'Day {man.day_counter}\nДоброе утро, {man.name}! hp - {man.health}')
    action = input("Выберите действие: ")
    if action == 'menu':
        while True:
            print(
                "Игра приостановлена\ncont - продолжить игру\nexit - выйти из игры\ndel - удалить сохранение")
            menu_action = input(":")
            if menu_action == "cont":
                break
            elif menu_action == "exit":
                break
            elif menu_action == "del":
                if len(saves) < 1:
                    print("Нет лишних сохранений")
                    break
                else:
                    print(glob.glob("*.pkl"))
                    delete_save = input("Введите сохранение для удаления(до точки)\n:")
                    os.remove(delete_save + ".pkl")
                    print(f"Сохранение {delete_save + ".pkl"} удалено")
            else:
                print(f"неизвестное действие - {menu_action}")
        if menu_action == 'exit':
            print(f"Конец игры, до встречи, {character_name}!")
            break
    elif action == 'help':
        print(commands)
    else:
        if action in ACTIONS_MENU:
            if action in tiredness_list:
                if getattr(man, 'tiredness') < TirednessParameters.MAXIMUM.value:
                    getattr(man, ACTIONS_MENU[action])()
                    man.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE.value
                else:
                    print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                          f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать\n"
                          f"heal - полечиться у врача\nmeditate - помедитировать\ncook - приготовить еды\n"
                          f"read - почитать книгу")
            else:
                getattr(man, ACTIONS_MENU[action])()
            if not getattr(man, 'alive'):
                break
            if getattr(man, 'rang') == "Lord":
                print(f"Вы достигли вершины! Ранга Лорд, поздравляем")
                contin = input("Желаете играть дальше? y/n\n:")
                if contin == "n":
                    print(f"Конец игры, до встречи, {character_name}!")
                    break
                elif contin == 'y':
                    continue
                else:
                    print(f"неизвестное действие -= {contin}")
            save(man, man.name)
        else:
            print(f"Неизвестное действие - {action}")

