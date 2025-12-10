from class_man import Man

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
}

while True:
    print("Вы играли раньше?\nНапишите\nда\nнет")
    played = input()
    if played == "да":
        man = Man.load('man.pkl')
        character_name = man.name
        print("Возможные действия:\n"
              "self - информация о себе\n"
              "eat - поесть\n"
              "shopping - купить еды\n"
              "work - пойти работать\n"
              "gym - пойти в качалку\n"
              "study - пойти на учёбу\n"
              "fight - участвовать в бою\n"
              "sleep - пойти спать\n"
              "heal - полечиться у врача\n"
              "exit - выйти из игры\n"
              "help - список действий\n")
        break
    elif played == "нет":
        character_name = input('Введите имя персонажа: ')
        print(f"Добро пожаловать, {character_name}")
        man = Man(character_name)
        print("Возможные действия:\n"
          "self - информация о себе\n"
          "eat - поесть\n"
          "shopping - купить еды\n"
          "work - пойти работать\n"
          "gym - пойти в качалку\n"
          "study - пойти на учёбу\n"
          "fight - участвовать в бою\n"
          "sleep - пойти спать\n"
          "heal - полечиться у врача\n"
          "exit - выйти из игры\n"
          "help - список действий\n")
        break
    else:
        print(f"выберите еще раз")

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
        else:
            print(f"Неизвестное действие - {action}")
    else:
        print(f"Конец игры, до встречи, {character_name}!")
        break

