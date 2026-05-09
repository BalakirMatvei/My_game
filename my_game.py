import os
import pickle
from class_man import Man
import glob
from constants import TirednessParameters
from rich.console import Console
from rich import print
console = Console()

ACTIONS_MENU = {
    "self": "print",
    "eat": "eat",
    "shop": "shopping",
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

commands = ("[italic purple]Возможные действия[/]:\n"
            "[bold purple]self[/] - информация о себе         [bold purple]eat[/] - поесть\n"
            "[bold purple]cook[/] - приготовить еды           [bold purple]shop[/] - купить еды\n"
            "[bold purple]work[/] - пойти работать            [bold purple]gym[/] - пойти в качалку\n"
            "[bold purple]study[/] - пойти на учёбу           [bold purple]fight[/] - участвовать в бою\n"
            "[bold purple]sleep[/] - пойти спать              [bold purple]heal[/] - полечиться у врача\n"
            "[bold purple]menu[/] - открыть меню              [bold purple]invest[/] - инвестировать\n"
            "[bold purple]help[/] - список действий           [bold purple]casino[/] - пойти в казино\n"
            "[bold purple]date[/] - сходить на свидание       [bold purple]meditate[/] - помедитировать\n"
            "[bold purple]read[/] - почитать книгу")

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
        print(f"[bold]Добро пожаловать, {character_name}[/]")
        man = Man(character_name)
        print(commands)
        break
    else:
        played = console.input("[bold blue]новая игра[/] или [bold green]загрузить[/](Введите [bold blue]n[/] или [bold green]l[/]):\n")
        if played == 'n':
            character_name = input('Введите имя персонажа: ')
            print(f"[bold]Добро пожаловать, {character_name}[/]")
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
            print(f'[bold red]неизвестное действие[/] - {played}')

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
                    print(f"Сохранение {delete_save} удалено")
            else:
                print(f"[bold red]неизвестное действие[/] - {menu_action}")
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
                    print(f"[red]Вы слишком устали сегодня[/]\nОставшиеся действия на сегодня:\n"
                          f"[bold purple]self[/] - информация о себе\n[bold purple]eat[/] - поесть\n[bold purple]shopping[/] - купить еды\n[bold purple]sleep[/] - пойти спать\n"
                          f"[bold purple]heal[/] - полечиться у врача\n[bold purple]meditate[/] - помедитировать\n[bold purple]cook[/] - приготовить еды\n"
                          f"[bold purple]read[/] - почитать книгу")
            else:
                getattr(man, ACTIONS_MENU[action])()
            if not getattr(man, 'alive'):
                break
            if getattr(man, 'rang') == "Lord":
                print(f"[bold yellow on blue]Вы достигли вершины![/] Ранга Лорд, [bold blink]поздравляем[/]")
                cont = input("Желаете играть дальше? y/n\n:")
                if cont == "n":
                    print(f"Конец игры, до встречи, {character_name}!")
                    break
                elif cont == 'y':
                    continue
                else:
                    print(f"[bold red]неизвестное действие[/] -= {cont}")
            save(man, man.name)
        else:
            print(f"[bold red]неизвестное действие[/] - {action}")

