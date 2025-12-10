from constants import WorkParameters, EatParameters, IntelligenceLVL, \
    ShoppingParameters, GymParameters, StudyParameters, SleepParameters, \
    SalaryParameters, TirednessParameters, RangParameters, HealParameters, \
    AgeParameters, BD_GIFT_MONEY, FightParameters, StressParameters

import random
import pickle

class Man:
    RangList = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster"]

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
        self.rang = "Bronze"
        self.age = 18
        self.stress = 0

    def __str__(self):
        return f"{self.name}, возраст - {self.age}, сытость - {self.fullness}, hp - {self.health}" \
               f", баланс - {self.money}$, еда - {self.food}, " \
               f"сила - {self.strength}, интеллект - {self.intelligence}, усталость - {self.tiredness}, Ранг - {self.rang}, {self.stress} "

    def print(self):
        print(self)

    def eat(self):
        if self.food >= EatParameters.MINIMUM_FOOD:
            self.food -= EatParameters.REDUCE_FOOD
            self.fullness += EatParameters.INCREASE_FULLNESS
            if self.fullness > EatParameters.MAXIMUM_FULLNESS:
                self.fullness = EatParameters.MAXIMUM_FULLNESS.value
            print(f'Вы поели\nсытость - {self.fullness}\nеды осталось - {self.food}')
        else:
            print(f'у вас нет еды\nеды осталось - {self.food}')

    def shopping(self):
        if self.money >= ShoppingParameters.MINIMUM_MONEY:
            self.food += ShoppingParameters.INCREASE_FOOD
            self.money -= ShoppingParameters.REDUCE_MONEY
            print(f'Вы купили еды!\nеды осталось - {self.food}\nбаланс - {self.money}$')
        else:
            print(f'у вас нет денег:(\nбаланс - {self.money}$\nстоимость еды - {ShoppingParameters.MINIMUM_MONEY.value}$)')

    def gym(self):
        if self.tiredness < TirednessParameters.MAXIMUM:
            if self.stress == StressParameters.MAXIMUM:
                self.health -= StressParameters.HEALTH_REDUCE.value
            if self.age >= AgeParameters.OLD:
                if self.fullness >= AgeParameters.REDUCE_FULLNESS_OLDS:
                    self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
                    self.strength += AgeParameters.LIMITATION_STRENGTH_OLD
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                    self.stress += StressParameters.STRESS_INCREASE
                    if self.stress > StressParameters.MAXIMUM:
                        self.stress = StressParameters.MAXIMUM.value
                    print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
                else:
                    print(f'Вы слишком голодны\nсытость - {self.fullness}\nсытости потратится - {AgeParameters.REDUCE_FULLNESS_OLDS.value}')
            elif self.age >= AgeParameters.ADULT:
                if self.fullness >= AgeParameters.REDUCE_FULLNESS_ADULTS:
                    self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
                    self.strength += AgeParameters.LIMITATION_STRENGTH_ADULT
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_ADULTS
                    self.stress += StressParameters.STRESS_INCREASE
                    if self.stress > StressParameters.MAXIMUM:
                        self.stress = StressParameters.MAXIMUM.value
                    print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
                else:
                    print(f'Вы слишком голодны\nсытость - {self.fullness}\nсытости потратится - {AgeParameters.REDUCE_FULLNESS_ADULTS.value}')
            else:
                if self.fullness >= GymParameters.MINIMUM_FULLNESS:
                     self.strength += GymParameters.INCREASE_STRENGTH
                     self.fullness -= GymParameters.REDUCE_FULLNESS
                     self.stress += StressParameters.STRESS_INCREASE
                     if self.stress > StressParameters.MAXIMUM:
                         self.stress = StressParameters.MAXIMUM.value
                     print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
                else:
                     print(f'у вас нет сил:(\nсытость - {self.fullness}, сытости потратится - {GymParameters.REDUCE_FULLNESS.value})')
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать\nheal - полечиться у врача")

    def work(self):
        if self.tiredness < TirednessParameters.MAXIMUM:
            self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
            self.stress += StressParameters.STRESS_INCREASE
            if self.stress > StressParameters.MAXIMUM:
                self.stress = StressParameters.MAXIMUM.value
            if self.stress == StressParameters.MAXIMUM:
                self.health -= StressParameters.HEALTH_REDUCE.value
            if self.intelligence >= IntelligenceLVL.EXTRA_HIGH:
                self.money += SalaryParameters.EXTRA_HIGH
            elif self.intelligence >= IntelligenceLVL.VERY_HIGH:
                self.money += SalaryParameters.VERY_HIGH
            elif self.intelligence >= IntelligenceLVL.HIGH:
                self.money += SalaryParameters.HIGH
            elif self.intelligence >= IntelligenceLVL.MEDIUM:
                self.money += SalaryParameters.MEDIUM
            else:
                self.money += SalaryParameters.MINIMUM
            if self.age >= AgeParameters.OLD:
                if self.fullness >= AgeParameters.REDUCE_FULLNESS_OLDS:
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                    print(f"Вы заработали денег!\nбаланс - {self.money}$\nсытость - {self.fullness}")
                else:
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                    self.health -= WorkParameters.REDUCE_HEALTH
                    if self.health <= 0:
                        Man.death(self)
                    else:
                        print(f'Ого! Вы пошли на работу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nбаланс - {self.money}$')
            elif self.age >= AgeParameters.ADULT:
                if self.fullness >= AgeParameters.REDUCE_FULLNESS_ADULTS:
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_ADULTS
                    print(f"Вы заработали денег!\nбаланс - {self.money}$\nсытость - {self.fullness}")
                else:
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                    self.health -= WorkParameters.REDUCE_HEALTH
                    if self.health <= 0:
                        Man.death(self)
                    else:
                        print(f'Ого! Вы пошли на работу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nбаланс - {self.money}$')
            else:
                if self.fullness >= WorkParameters.REDUCE_FULLNESS:
                    self.fullness -= WorkParameters.REDUCE_FULLNESS
                    print(f"Вы заработали денег!\nбаланс - {self.money}$\nсытость - {self.fullness}")
                else:
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                    self.health -= WorkParameters.REDUCE_HEALTH
                    if self.health <= 0:
                        Man.death(self)
                    else:
                        print(
                            f'Ого! Вы пошли на работу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nбаланс - {self.money}$')
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать\nheal - полечиться у врача")

    def study(self):
        if self.tiredness < TirednessParameters.MAXIMUM:
            self.tiredness += TirednessParameters.FOR_SINGLE_ACTIVE
            self.stress += StressParameters.STRESS_INCREASE
            if self.stress > StressParameters.MAXIMUM:
                self.stress = StressParameters.MAXIMUM.value
            if self.stress == StressParameters.MAXIMUM:
                self.health -= StudyParameters.REDUCE_HEALTH.value
            if self.age >= AgeParameters.OLD:
                if self.fullness >= AgeParameters.REDUCE_FULLNESS_OLDS:
                    self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                    print(f'Вы стали умнее!\nинтеллект - {self.intelligence}\nсытость - {self.fullness}')
                else:
                    self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                    self.health -= StudyParameters.REDUCE_HEALTH
                    if self.health <= 0:
                        Man.death(self)
                    else:
                        print(
                            f'Ого! Вы пошли на учебу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nинтеллект - {self.intelligence}')
            elif self.age >= AgeParameters.ADULT:
                if self.fullness >= AgeParameters.REDUCE_FULLNESS_ADULTS:
                    self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                    self.fullness -= AgeParameters.REDUCE_FULLNESS_ADULTS
                    print(f'Вы стали умнее!\nинтеллект - {self.intelligence}\nсытость - {self.fullness}')
                else:
                    self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                    self.health -= StudyParameters.REDUCE_HEALTH
                    if self.health <= 0:
                        Man.death(self)
                    else:
                        print(
                            f'Ого! Вы пошли на учебу несмотря на сильный голод, но потеряли hp\nhp - {self.health}\nинтеллект - {self.intelligence}')
            else:
                self.intelligence += StudyParameters.INCREASE_INTELLIGENCE
                self.fullness -= StudyParameters.REDUCE_FULLNESS
                print(f'Вы стали умнее!\nинтеллект - {self.intelligence}\nсытость - {self.fullness}')
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать\nheal - полечиться у врача")

    def death(self):
        self.alive = False
        print(f"Вы умерли:(\nДней прожито - {self.day_counter - 1}")

    def sleep(self):
        self.day_counter += 1
        if self.day_counter % 50 == 0:
            self.age += 1
            print(f"Сегодня ваш день рождения, поздравляем!!!\n"
                  f"Вам исполнилось {self.age}\n"
                  f"Небольшой подарок от нас!\n"
                  f"+ 100$")
            self.money += BD_GIFT_MONEY
            print(f"баланс - {self.money}")
        if self.money >= RangParameters.MONEY_GRANDMASTER:
            self.r = 6
        elif self.money >= RangParameters.MONEY_MASTER:
            self.r = 5
        elif self.money >= RangParameters.MONEY_DIAMOND:
            self.r = 4
        elif self.money >= RangParameters.MONEY_PLATINUM:
            self.r = 3
        elif self.money >= RangParameters.MONEY_GOLD:
            self.r = 2
        elif self.money >= RangParameters.MONEY_SILVER:
            self.r = 1
        else:
            self.r = 0
        if self.stress < StressParameters.MAXIMUM:
            self.fullness -= SleepParameters.REDUCE_FULLNESS
            self.tiredness = 0
            if self.fullness <= 0:
                self.health -= SleepParameters.REDUCE_HEALTH
                self.fullness = 0
            if self.health <= 0:
                Man.death(self)
            if self.health > SleepParameters.MAXIMUM_HEALTH:
                self.health = SleepParameters.MAXIMUM_HEALTH.value
            self.rang = self.RangList[self.r]
            if self.rang == "Grandmaster":
                print(f"Поздравляю, вы достигли ранга Grandmaster в возрасте {self.age} и прошли игру!\n"
                      "Спасибо за игру! ")
            else:
                print(f"Ваш ранг - {self.rang}")
            self.save()
        else:
            self.health -= StressParameters.HEALTH_REDUCE.value

    def commands(self):
        print("Возможные действия:\n"
              "self - информация о себе\n"
              "eat - поесть\n"
              "shopping - купить еды\n"
              "work - пойти работать\n"
              "gym - пойти в качалку\n"
              "study - пойти на учёбу\n"
              "fight - участвовать в бою"
              "sleep - пойти спать\n"
              "exit - выйти из игры\n"
              "help - список действий\n")

    def heal(self):
        if self.money >= HealParameters.MONEY_REDUCE:
            self.health += HealParameters.HEALTH_INCREASE
            self.money -= HealParameters.MONEY_REDUCE
            if self.health > SleepParameters.MAXIMUM_HEALTH:
                self.health = SleepParameters.MAXIMUM_HEALTH.value
            print(f"Вы полечились у врача!\nhp - {self.health}\nбаланс - {self.money}$")
        else:
            print(f"У вас нет денег\nбаланс - {self.money}$\nстоимость лечения - {HealParameters.MONEY_REDUCE.value}$")

    def fight(self):
        if self.tiredness < TirednessParameters.MAXIMUM.value:
            if self.fullness >= FightParameters.MINIMUM_FULLNESS.value:
                self.tiredness = TirednessParameters.MAXIMUM.value
                self.fullness -= FightParameters.FULLNESS_REDUCE
                if self.strength >= FightParameters.STRENGTH_INCREASED_CHANCE:
                    if random.randint(0, 100) <= FightParameters.INCREASED_WIN_CHANCE:
                        self.money += FightParameters.MONEY_WIN
                        self.health = FightParameters.HEALTH_REDUCE_WIN.value
                        if self.health == 0:
                            self.health = FightParameters.HEALTH_AFTER_LOOS.value
                        print(f"Вы выиграли бой местной лиги!!!\nВаш гонорар - {FightParameters.MONEY_WIN.value}$\nВы сильно устали, советуем поесть")
                    else:
                        self.money += FightParameters.MONEY_LOOS
                        self.health = FightParameters.HEALTH_AFTER_LOOS.value
                        self.stress += FightParameters.STRENGTH_INCREASED_CHANCE
                        print(f"Вы проиграли бой местной лиги:(\nВаш гонорар - {FightParameters.MONEY_LOOS.value}$\nВы сильно устали, советуем поесть")
                elif self.strength >= FightParameters.MINIMUM_STRENGTH:
                    if random.randint(0, 100) <= FightParameters.DEFAULT_WIN_CHANCE:
                        self.money += FightParameters.MONEY_WIN
                        self.health -= FightParameters.HEALTH_REDUCE_WIN.value
                        if self.health == 0:
                            self.health = FightParameters.HEALTH_AFTER_LOOS.value
                        print(f"Вы выиграли бой местной лиги!!!\nВаш гонорар - {FightParameters.MONEY_WIN.value}$\nВы сильно устали, советуем поесть")
                    else:
                        self.money += FightParameters.MONEY_LOOS
                        self.health = FightParameters.HEALTH_AFTER_LOOS.value
                        self.stress += FightParameters.STRESS_LOOS
                        print(f"Вы проиграли бой местной лиги:(\nВаш гонорар - {FightParameters.MONEY_LOOS.value}$\nВы сильно устали, советуем поесть")
                else:
                    print(f"Вы недостаточно сильны для участия в боях местной лиги:(\n"
                          f"Ваша сила - {self.strength}\n"
                          f"Минимальная сила для участия - {FightParameters.MINIMUM_STRENGTH.value}")
            else:
                print(f"У вас мало сил для боя\nсытость - {self.fullness}\nминимальна сытость для боя - {FightParameters.MINIMUM_FULLNESS.value}")
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать\nheal - полечиться у врача")

    def save(self):
        with open('man.pkl', 'wb') as f:
            pickle.dump(self, f)

    def load(self):
        with open('man.pkl', 'rb') as f:
            return pickle.load(f)