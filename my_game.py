import pickle

from class_man import Man
import glob

ACTIONS_MENU = {
    "self": "print",
    "eat": "eat",
    "shopping": "shopping",
    "work": "work",
    "gym": "gym",
    "study": "study",
    "sleep": "sleep",
    "help": "commands",
    "heal": "heal",
    "fight": "fight",
    "cook": "cook",
}


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
        print("Возможные действия:\n"
              "self - информация о себе         eat - поесть\n"
              "cook - приготовить еды           shopping - купить еды\n"
              "work - пойти работать            gym - пойти в качалку\n"
              "study - пойти на учёбу           fight - участвовать в бою\n"
              "sleep - пойти спать              heal - полечиться у врача\n"
              "exit - выйти из игры             help - список действий\n")
        break
    else:
        played = input("новая игра или загрузить(Введите n или l):\n")
        if played == 'n':
            character_name = input('Введите имя персонажа: ')
            print(f"Добро пожаловать, {character_name}")
            man = Man(character_name)
            print("Возможные действия:\n"
                  "self - информация о себе         eat - поесть\n"
                  "cook - приготовить еды           shopping - купить еды\n"
                  "work - пойти работать            gym - пойти в качалку\n"
                  "study - пойти на учёбу           fight - участвовать в бою\n"
                  "sleep - пойти спать              heal - полечиться у врача\n"
                  "exit - выйти из игры             help - список действий\n")
            break
        elif played == 'l':
            print(glob.glob('*.pkl'))
            file_name = input("Введите название сохранения до точки ")
            man = load(file_name)
            character_name = man.name
            print("Возможные действия:\n"
                  "self - информация о себе         eat - поесть\n"
                  "cook - приготовить еды           shopping - купить еды\n"
                  "work - пойти работать            gym - пойти в качалку\n"
                  "study - пойти на учёбу           fight - участвовать в бою\n"
                  "sleep - пойти спать              heal - полечиться у врача\n"
                  "exit - выйти из игры             help - список действий\n")
            break
        else:
            print(f'неизвестное действие - {played}')

action = ""
while True:
    if getattr(man, 'alive') and action == "sleep":
        print(f'Day {man.day_counter}\nДоброе утро, {man.name}! hp - {man.health}')
    action = input("Выберите действие: ")
    if action != "exit":
        if action in ACTIONS_MENU:
            getattr(man, ACTIONS_MENU[action])()
            if not getattr(man, 'alive'):
                break
            if getattr(man, 'rang') == "Grandmaster":
                break
            save(man, man.name)
        else:
            print(f"Неизвестное действие - {action}")
    else:
        print(f"Конец игры, до встречи, {character_name}!")
        break

