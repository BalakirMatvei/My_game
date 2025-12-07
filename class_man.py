from constants import WorkParameters, EatParameters, IntelligenceLVL, \
    ShoppingParameters, GymParameters, StudyParameters, SleepParameters, \
    SalaryParameters, TirednessParameters


class Man:
    ranglist = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster"]

    def __init__(self, name):
        self.name = name
        self.fullness = 80
        self.money = 50
        self.health = 100
        self.food = 100
        self.strength = 50
        self.intelligence = 50
        self.day_counter = 1
        self.alive = True
        self.tiredness = 0
        self.r = 0
        self.rang = ranglist[r]

    def __str__(self):
        return f"{self.name}, сытость - {self.fullness}, hp - {self.health}" \
               f", баланс - {self.money}$, еда - {self.food}, " \
               f"сила - {self.strength}, интеллект - {self.intelligence}, усталость - {self.tiredness} "

    def print(self):
        print(self)

    def eat(self):
        if self.food >= EatParameters.MINIMUM_FOOD:
            self.food -= EatParameters.REDUCE_FOOD
            self.fullness += EatParameters.INCREASE_FULLNESS
            if self.fullness > EatParameters.MAXIMUM_FULLNESS:
                self.fullness = EatParameters.MAXIMUM_FULLNESS
        else:
            print(f'у вас нет еды\nеды осталось - {self.food}')
        print(f'Вы поели\n сытость - {self.fullness}\nеды осталось - {self.food}')

    def shopping(self):
        if self.money >= ShoppingParameters.MINIMUM_MONEY:
            self.food += ShoppingParameters.INCREASE_FOOD
            self.money -= ShoppingParameters.REDUCE_MONEY
            print(f'Вы купили еды!\nеды осталось - {self.food}\nбаланс - {self.money}$')
        else:
            print(f'у вас нет денег:(\nбаланс - {self.money}$')

    def work(self):
        if self.tiredness < TirednessParameters.MAXIMUM:
            self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
            if self.fullness >= WorkParameters.MINIMUM_FULLNESS:
                if self.intelligence < IntelligenceLVL.MEDIUM:
                    self.money += SalaryParameters.MINIMUM
                elif self.intelligence < IntelligenceLVL.HIGH:
                    self.money += SalaryParameters.MEDIUM
                else:
                    self.money += SalaryParameters.HIGH.value
                self.fullness -= WorkParameters.REDUCE_FULLNESS
                print(f'Вы заработали денег!\nбаланс - {self.money}$\nсытость - {self.fullness}')
            else:
                self.money += SalaryParameters.MINIMUM
                self.fullness -= WorkParameters.REDUCE_FULLNESS
                self.health -= WorkParameters.REDUCE_HEALTH
                if self.health <= 0:
                    Man.death(self)
                else:
                    print(f'Ого! Вы пошли на работу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nбаланс - {self.money}$')
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать")

    def gym(self):
        if self.tiredness < TirednessParameters.MAXIMUM:
            self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
            if self.fullness >= GymParameters.MINIMUM_FULLNESS:
                self.strength += GymParameters.INCREASE_STRENGTH
                self.fullness -= GymParameters.REDUCE_FULLNESS
                print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
            else:
                print(f'у вас нет сил:(\nсытость - {self.fullness}')
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать")

    def study(self):
        if self.tiredness < TirednessParameters.MAXIMUM:
            self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
            if self.fullness >= StudyParameters.MINIMUM_FULLNESS:
                self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                self.fullness -= StudyParameters.REDUCE_FULLNESS
                print(f'Вы стали умнее!\nинтеллект - {self.intelligence}\nсытость - {self.fullness}')
            else:
                self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                self.health -= StudyParameters.REDUCE_HEALTH
                if self.health <= 0:
                    Man.death(self)
                else:
                    print(f'Ого! Вы пошли на учебу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nинтеллект - {self.intelligence}')
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать")

    def death(self):
        self.alive = False
        print(f"Вы умерли:(\nДней прожито - {self.day_counter - 1}")

    def sleep(self):
        self.day_counter += 1
        self.fullness -= SleepParameters.REDUCE_FULLNESS
        self.tiredness = 0
        if self.fullness <= 0:
            self.health -= SleepParameters.REDUCE_HEALTH
            self.fullness = 0
        else:
            self.health += SleepParameters.INCREASE_HEALTH
        if self.health <= 0:
            Man.death(self)
        if self.health > SleepParameters.MAXIMUM_HEALTH:
            self.health = SleepParameters.MAXIMUM_HEALTH.value

    def commands(self):
        print("Возможные действия:\n"
              "self - информация о себе\n"
              "eat - поесть\n"
              "shopping - купить еды\n"
              "work - пойти работать\n"
              "gym - пойти в качалку\n"
              "study - пойти на учёбу\n"
              "sleep - пойти спать\n"
              "exit - выйти из игры\n"
              "help - список действий\n")

