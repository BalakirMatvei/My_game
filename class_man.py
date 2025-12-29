from constants import WorkParameters, EatParameters, IntelligenceLVL, \
    ShoppingParameters, GymParameters, StudyParameters, SleepParameters, \
    SalaryParameters, TirednessParameters, RangParameters, HealParameters, \
    AgeParameters, BD_GIFT_MONEY, FightParameters, StressParameters, CookingParameters, InvestParameters, BJ_Cards, \
    BJ_Points, ROULETTE, DateParameters, MeditateParameters, ReadParameters

import random
import time

class Man:
    RangList = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster", "Lord"]

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
        self.single = True
        self.girl_rate = 0

    def __str__(self):
        return f"{self.name}, возраст - {self.age}, сытость - {self.fullness}, hp - {self.health}" \
               f", баланс - {self.money}$, еда - {self.food}, " \
               f"сила - {self.strength}, интеллект - {self.intelligence}, усталость - {self.tiredness}, Ранг - {self.rang}, холостяк - {self.single} "

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
        if self.age >= AgeParameters.OLD:
            if self.fullness >= AgeParameters.REDUCE_FULLNESS_OLDS:
                self.strength += AgeParameters.LIMITATION_STRENGTH_OLD
                self.fullness -= AgeParameters.REDUCE_FULLNESS_OLDS
                self.stress += StressParameters.STRESS_INCREASE
                if self.stress > StressParameters.MAXIMUM:
                    self.stress = StressParameters.MAXIMUM.value
                print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
            else:
                print(
                    f'Вы слишком голодны\nсытость - {self.fullness}\nсытости потратится - {AgeParameters.REDUCE_FULLNESS_OLDS.value}')
        elif self.age >= AgeParameters.ADULT:
            if self.fullness >= AgeParameters.REDUCE_FULLNESS_ADULTS:
                self.strength += AgeParameters.LIMITATION_STRENGTH_ADULT
                self.fullness -= AgeParameters.REDUCE_FULLNESS_ADULTS
                self.stress += StressParameters.STRESS_INCREASE
                if self.stress > StressParameters.MAXIMUM:
                    self.stress = StressParameters.MAXIMUM.value
                print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
            else:
                print(
                    f'Вы слишком голодны\nсытость - {self.fullness}\nсытости потратится - {AgeParameters.REDUCE_FULLNESS_ADULTS.value}')
        else:
            if self.fullness >= GymParameters.REDUCE_FULLNESS:
                self.strength += GymParameters.INCREASE_STRENGTH
                self.fullness -= GymParameters.REDUCE_FULLNESS
                self.stress += StressParameters.STRESS_INCREASE
                if self.stress > StressParameters.MAXIMUM:
                    self.stress = StressParameters.MAXIMUM.value
                print(f'Вы стали сильнее!\nсила - {self.strength}\nсытость - {self.fullness}')
            else:
                print(
                    f'у вас нет сил:(\nсытость - {self.fullness}, сытости потратится - {GymParameters.REDUCE_FULLNESS.value})')

    def work(self):
        self.stress += StressParameters.STRESS_INCREASE
        if self.stress > StressParameters.MAXIMUM:
            self.stress = StressParameters.MAXIMUM.value
        if self.stress == StressParameters.MAXIMUM.value:
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

    def study(self):
        self.stress += StressParameters.STRESS_INCREASE
        if self.stress > StressParameters.MAXIMUM:
            self.stress = StressParameters.MAXIMUM.value
        if self.stress == StressParameters.MAXIMUM.value:
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

    def death(self):
        self.alive = False
        print(f"Вы умерли:(\nДней прожито - {self.day_counter - 1}")

    def sleep(self):
        self.day_counter += 1
        if self.day_counter % 10 == 0:
            self.age += 1
            print(f"Сегодня ваш день рождения, поздравляем!!!\n"
                  f"Вам исполнилось {self.age}\n"
                  f"Небольшой подарок от нас!\n"
                  f"+ 100$")
            self.money += BD_GIFT_MONEY
            print(f"баланс - {self.money}")
        if self.money >= RangParameters.MONEY_LORD:
            self.r = 7
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
            if self.rang == "Lord":
                print(f"Поздравляю, вы достигли ранга Lord в возрасте {self.age} и прошли игру!\n"
                      "Спасибо за игру! ")
            else:
                print(f"Ваш ранг - {self.rang}")
        else:
            self.health -= StressParameters.HEALTH_REDUCE.value

    def commands(self):
        print("Возможные действия:\n"
              "self - информация о себе         eat - поесть\n"
              "cook - приготовить еды           shopping - купить еды\n"
              "work - пойти работать            gym - пойти в качалку\n"
              "study - пойти на учёбу           fight - участвовать в бою\n"
              "sleep - пойти спать              heal - полечиться у врача\n"
              "menu - открыть меню              invest - инвестировать\n"
              "help - список действий           casino - пойти в казино\n"
              "date - сходить на свидание       meditate - помедитировать")

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
                if self.strength >= FightParameters.STRENGTH_INCREASED_CHANCE:
                    if random.randint(0, 100) <= FightParameters.INCREASED_WIN_CHANCE:
                        self.money += FightParameters.MONEY_WIN
                        self.health = FightParameters.HEALTH_REDUCE_WIN.value
                        self.tiredness = TirednessParameters.MAXIMUM.value
                        self.fullness -= FightParameters.FULLNESS_REDUCE
                        if self.health == 0:
                            self.health = FightParameters.HEALTH_AFTER_LOOSE.value
                        print(f"Вы выиграли бой местной лиги!!!\nВаш гонорар - {FightParameters.MONEY_WIN.value}$\nВы сильно устали, советуем поесть")
                    else:
                        self.money += FightParameters.MONEY_LOOSE
                        self.health = FightParameters.HEALTH_AFTER_LOOSE.value
                        self.stress += FightParameters.STRENGTH_INCREASED_CHANCE
                        self.fullness -= FightParameters.FULLNESS_REDUCE
                        print(f"Вы проиграли бой местной лиги:(\nВаш гонорар - {FightParameters.MONEY_LOOSE.value}$\nВы сильно устали, советуем поесть")
                elif self.strength >= FightParameters.MINIMUM_STRENGTH:
                    if random.randint(0, 100) <= FightParameters.DEFAULT_WIN_CHANCE:
                        self.money += FightParameters.MONEY_WIN
                        self.health -= FightParameters.HEALTH_REDUCE_WIN.value
                        self.tiredness = TirednessParameters.MAXIMUM.value
                        self.fullness -= FightParameters.FULLNESS_REDUCE
                        if self.health == 0:
                            self.health = FightParameters.HEALTH_AFTER_LOOSE.value
                        print(f"Вы выиграли бой местной лиги!!!\nВаш гонорар - {FightParameters.MONEY_WIN.value}$\nВы сильно устали, советуем поесть")
                    else:
                        self.money += FightParameters.MONEY_LOOSE
                        self.health = FightParameters.HEALTH_AFTER_LOOSE.value
                        self.stress += FightParameters.STRESS_LOOSE
                        self.fullness -= FightParameters.FULLNESS_REDUCE
                        print(f"Вы проиграли бой местной лиги:(\nВаш гонорар - {FightParameters.MONEY_LOOSE.value}$\nВы сильно устали, советуем поесть")
                else:
                    print(f"Вы недостаточно сильны для участия в боях местной лиги:(\n"
                          f"Ваша сила - {self.strength}\n"
                          f"Минимальная сила для участия - {FightParameters.MINIMUM_STRENGTH.value}")
            else:
                print(f"У вас мало сил для боя\nсытость - {self.fullness}\nминимальна сытость для боя - {FightParameters.MINIMUM_FULLNESS.value}")
        else:
            print(f"Вы слишком устали сегодня\nОставшиеся действия на сегодня:\n"
                  f"self - информация о себе\neat - поесть\nshopping - купить еды\nsleep - пойти спать\nheal - полечиться у врача")

    def cook(self):
        if self.food > 0:
            self.fullness += CookingParameters.FULLNESS_INCREASE
            if self.fullness > EatParameters.MAXIMUM_FULLNESS:
                self.fullness = EatParameters.MAXIMUM_FULLNESS.value
            self.stress -= CookingParameters.STRESS_REDUCE
            if self.stress < 0:
                self.stress = 0
            self.food -= EatParameters.REDUCE_FOOD
            print(f"Вы приготовили еды и поели\nсытость - {self.fullness}\nеды осталось - {self.food}")
        else:
            print(f"У вас нет еды\nеды осталось - {self.food}")

    def invest(self):
        profit = 0
        deposit = int(input(f"Введите сумму которую хотите инвестировать\n:"))
        if deposit >= InvestParameters.MINIMUM_DEPOSIT:
            if deposit <= self.money:
                self.money -= deposit
                if random.randint(1,100) < InvestParameters.CHANCE:
                    profit = deposit * random.randint(1,7)
                    self.money += profit
                    print(f"Ваша инвестиция принесла прибыль в размере - {profit}$!!!\n поздравляем!!!\n"
                          f"баланс - {self.money}")
                else:
                    print(f"Ваша инвестиция прогорела:(\n"
                          f"баланс - {self.money}")
            else:
                print(f"Вы не можете инвестировать больше чем у вас есть\n"
                      f"баланс - {self.money}")
        else:
            print(f"Минимальная инвестиция - {InvestParameters.MINIMUM_DEPOSIT.value}")

    def bj(self):
        while True:
            self_cards = []
            diller_cards = []
            bj_action = ''
            self_points = 0
            diller_points = 0
            win = False
            bj_action = input('начать игру или выйти? s или e?\n:')
            if bj_action == 'e':
                print("до встречи!")
                break
            elif bj_action == 's':
                print(f"баланс - {self.money}$")
                dep = int(input("Ставка\n:"))
                if dep <= self.money:
                    self.money -= dep
                    win = False
                    self_cards.append(BJ_Cards[random.randint(0, len(BJ_Cards) - 1)])
                    self_points += BJ_Points.get(self_cards[-1])
                    self_cards.append(BJ_Cards[random.randint(0, len(BJ_Cards) - 1)])
                    self_points += BJ_Points.get(self_cards[-1])
                    diller_cards.append(BJ_Cards[random.randint(0, len(BJ_Cards) - 1)])
                    diller_points += BJ_Points.get(diller_cards[-1])
                    print(f'Рука диллера - {diller_cards}, сумма - {diller_points}')
                    print(f'Ваша рука  - {self_cards}, сумма - {self_points}')
                    while True:
                        if self_points == 21:
                            print("Вы выиграли")
                            win = True
                            self.money += dep * 2
                            print(f"баланс - {self.money}$")
                            break
                        game_action = input('взять еще или хватит? h или s\n:')
                        if game_action == 'h':
                            self_cards.append(BJ_Cards[random.randint(0, len(BJ_Cards) - 1)])
                            self_points += BJ_Points.get(self_cards[-1])
                            if self_points > 21:
                                print(f'{self_cards}')
                                print("Перебор:(")
                                print(f"баланс - {self.money}$")
                                self_cards = []
                                diller_cards = []
                                self_points = 0
                                diller_points = 0
                                break
                            else:
                                print(f'Рука диллера - {diller_cards}, сумма - {diller_points}')
                                print(f'Ваша рука  - {self_cards}, сумма - {self_points}')
                        elif game_action == 's':
                            while True:
                                diller_cards.append(BJ_Cards[random.randint(0, len(BJ_Cards) - 1)])
                                diller_points += BJ_Points.get(self_cards[-1])
                                if diller_points > 21:
                                    print("У диллера перебор. Вы выиграли!")
                                    self_cards = []
                                    diller_cards = []
                                    self_points = 0
                                    diller_points = 0
                                    self.money += dep * 2
                                    win = True
                                    print(f"баланс - {self.money}$")
                                    break
                                elif 17 < diller_points < 21:
                                    if self_points > diller_points:
                                        print(f"Ваши очки - {self_points}\nОчки диллера - {diller_points}")
                                        print("Вы выиграли!")
                                        self_cards = []
                                        diller_cards = []
                                        self_points = 0
                                        diller_points = 0
                                        win = True
                                        self.money += dep * 2
                                        print(f"баланс - {self.money}$")
                                        break
                                    elif self_points < diller_points:
                                        print(f"Ваши очки - {self_points}\nОчки диллера - {diller_points}")
                                        print("Вы проиграли:(")
                                        self_cards = []
                                        diller_cards = []
                                        self_points = 0
                                        diller_points = 0
                                        win = True
                                        print(f"баланс - {self.money}$")
                                        break
                                    else:
                                        print(f"Ваши очки - {self_points}\nОчки диллера - {diller_points}")
                                        print("ничья")
                                        self_cards = []
                                        diller_cards = []
                                        self_points = 0
                                        diller_points = 0
                                        self.money += dep
                                        win = True
                                        print(f"баланс - {self.money}$")
                                        break
                            if win:
                                break
                        else:
                            print(f"неизвестное действие - {game_action}")
                else:
                    print(f'вы не можете поставить больше чем у вас есть\nбаланс - {self.money}')
            else:
                print(f"неизвестное действие - {bj_action}")

    def roulette(self):
        while True:
            roulette_action = ''
            print(f"баланс - {self.money}$")
            roulette_action = input('начать игру или выйти? s или e?\n:')
            if roulette_action == 'e':
                print(f"до встречи, {self.name}")
                break
            elif roulette_action == 's':
                bet_list = []
                dep_list = []
                # print(f"баланс - {self.money}$")
                print('    3', '6', '9', '12', '15', '18', '21', '24', '27', '30', '33', '36')
                print('0', '2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35')
                print('    1', '4', '7', '10', '13', '16', '19', '22', '25', '28', '31', '34')
                print('     1st 12      ', '    2nd 12     ', '       3rd 12')
                print('1-18 ', '    EVEN    ', 'red     ', 'black', '    ODD  ', '   19-36')
                while True:
                    print(f"баланс - {self.money}$")
                    bet = input('Выберите ставку: ')
                    if bet in ROULETTE.all_bets:
                        bet_list.append(bet)
                        print(f"баланс - {self.money}$")
                        dep = int(input("Сумма ставки: "))
                        if dep <= self.money:
                            dep_list.append(dep)
                            self.money -= dep
                        else:
                            print(f"У вас не хватает на такую ставку - {dep}")
                            dep_list.pop()
                    else:
                        print(f"нет такого варианта - {bet}")
                    if self.money > 0:
                        bet_action = input("Хотите поставить ещё? y/n\n:")
                        if bet_action == 'n':
                            break
                        elif bet_action != 'y':
                            print(f"нет такого варианта - {bet_action}")
                    else:
                        break
                if len(bet_list) > 0:
                    spin_result = random.choice(ROULETTE.all_results)
                    print("Поехали!")
                    time.sleep(1)
                    print("spinning")
                    time.sleep(1)
                    print('spinning')
                    time.sleep(1)
                    print('spinning')
                    time.sleep(1)
                    print(f"выпал номер {spin_result} {ROULETTE.colors.get(spin_result)}")
                    for num, i in enumerate(bet_list):
                        if i == '1st 12' and spin_result in ROULETTE.first_12:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == '2nd 12' and spin_result in ROULETTE.second_12:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == '3rd 12' and spin_result in ROULETTE.third_12:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == '1-18' and spin_result in ROULETTE.first_half:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == '19-36' and spin_result in ROULETTE.second_half:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == 'EVEN' and spin_result in ROULETTE.even:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == 'ODD' and spin_result in ROULETTE.odd:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == 'red' and spin_result in ROULETTE.red:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i == 'black' and spin_result in ROULETTE.black:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        elif i in ROULETTE.all_results and spin_result == i:
                            print(f"Ставка сыграла({i}), Ваш выигрыш - {dep_list[num] * ROULETTE.multipliers.get(i)}$")
                            self.money += dep_list[num] * ROULETTE.multipliers.get(i)
                        else:
                            print("Ваша ставка не сыграла")
                else:
                    print('Добавьте минимум 1 ставку')
            else:
                print(f"неизвестное действие - {roulette_action}")

    def casino(self):
        game = input("Во что хотите поиграть? bj/roulette\n:")
        if game == 'bj':
            self.bj()
        elif game == 'roulette':
            self.roulette()
        else:
            print(f"Неизвестное действие - {game}")

    def date(self):
        if self.single:
            girl_rate = 0
            chance = 0
            if self.money >= DateParameters.MINIMUM_MONEY:
                girl_rate = random.randint(DateParameters.MINIMUM_RATE, DateParameters.MAXIMUM_RATE)  # определение уровня девушки
                print(f"вы пригласили на свидание девушку {girl_rate}/10")
                if girl_rate < DateParameters.AVERAGE_RATE:
                    chance = DateParameters.MAXIMUM_GIRL_CHANCE
                elif girl_rate < DateParameters.MAXIMUM_RATE:
                    chance = DateParameters.AVERAGE_GIRL_CHANCE
                else:
                    chance = DateParameters.MINIMUM_GIRL_CHANCE

                while True:  # выбор места
                    location = input("выберите место для свидания\nпарк     кафе    ресторан\n1/2/3\n:")
                    if location == "1" or location == "2" or location == "3":
                        chance += DateParameters.location_chance.get(location)
                        break
                    else:
                        print(f"Неизвестное место - {location}")
                print(f"-вы встретились и пошли {DateParameters.location_action.get(location)}")

                if self.intelligence <= DateParameters.INTELLIGENCE_TALK:  # оценка интеллекта
                    print("-но разговор не пошел:(")
                    print("-вы весь вечер вытались найти темы для разговора и шутить, но вышло так себе")
                    chance -= DateParameters.NOT_TALK_CHANCE_DECREASE
                else:
                    print("-и разговор завязался")
                    print("-вы весь вечер блистали своим остроумием и шутили, она оценила ваш интеллект")
                    chance += DateParameters.TALK_CHANCE_INCREASE

                while True:  # разговор о деньгах
                    print("-слово за слово и она спросила о вашем финансовом положении")
                    print("Д: извини за вопрос, но сколько у тебя на счету?")
                    money_action = input("честно сказать    увильнуть от ответа\n1/2\n:")
                    if money_action == "1":
                        print(f"Вы: {self.money}")
                        if self.money >= DateParameters.MONEY_UP_CHANCE:
                            print("Д: ого, а ты богач")
                            chance += DateParameters.CHANCE_UP_FOR_SELF
                        else:
                            print("Д: не густо")
                            chance -= DateParameters.CHANCE_DOWN_FOR_SELF
                        break
                    elif money_action == "2":
                        phrase = input('что ей скажешь?\n'
                                       'не переживай, я при бабках     1\n'
                                       'на жизнь хватает               2\n'
                                       'пока на мели                   3\n'
                                       '1/2/3\n'
                                       ':')
                        print(f"Вы: {DateParameters.phrase_variants.get(phrase)}")
                        if phrase == '1':
                            decision = random.randint(1, 2)
                            if decision == 1:
                                print("-она вам поверила!")
                                chance += DateParameters.CHANCE_UP_FOR_SELF
                            else:
                                print("-она посчитала вас очередным воздуханом:(")
                                chance -= DateParameters.CHANCE_DOWN_FOR_SELF
                            break
                        elif phrase == '2':
                            decision = random.randint(1, 2)
                            if decision == 1:
                                print("-она сочла это достойным ответом")
                                chance += DateParameters.CHANCE_UP_FOR_SELF
                            else:
                                print("-она решила, что этого мало")
                                chance -= DateParameters.CHANCE_DOWN_FOR_SELF
                        else:
                            print("-она расстроилась, но не подала виду")
                            chance -= DateParameters.CHANCE_DOWN_FOR_SELF
                            break
                    else:
                        print(f"неизвестное действие - {money_action}")

                if location == '2':  # оплата
                    self.money -= DateParameters.location_chance.get(location)
                    print(
                        f"-вы оплатили ваш счет в кафе, он вам вышел - {DateParameters.location_money.get(location)}$")
                elif location == '3':
                    self.money -= DateParameters.location_money.get(location)
                    print(
                        f"-вы оплатили ваш счет в ресторане, он вам вышел - {DateParameters.location_money.get(location)}$")

                while True:  # дорога домой
                    home_action = input('провести ее домой      попращаться на месте\n1/2\n:')
                    if home_action == "1":
                        if self.strength >= DateParameters.STRENGTH_UP_CHANCE:
                            print("-вы провели её домой, по дороге она оценила ваше спортивное телослжение:)")
                            chance += DateParameters.CHANCE_UP_FOR_SELF
                        else:
                            print("-вы провели её домой")
                        break
                    elif home_action == "2":
                        print("-вы попрощались на месте, из-за этого она не успела оценить вашу физическую форму ")
                        break
                    else:
                        print(f"неизвестное действие - {home_action}")

                result = random.randint(0, 100)  # итог
                print("-уже дома вы написали ей и предложили отношения")
                if result <= chance:
                    self.single = False
                    print(f'-она согласилась! вы восхитили ее и заполучили девушку {girl_rate}/10, поздравляю!')
                    self.girl_rate = girl_rate
                else:
                    print("-вы ее не впечатлили и она вам отказала:(")
            else:
                print(f"у вас маловато денег, надо хотя бы - {DateParameters.MINIMUM_MONEY}$")
        else:
            print(f"у вас уже есть девушка {self.girl_rate}/10")
            break_up_action = input(f"-хотите расстаться со своей {self.girl_rate}/10\ny/n\n:")
            while True:
                if break_up_action == "y":
                    self.single = True
                    print("вы расстались")
                    break
                elif break_up_action == "n":
                    break
                else:
                    print(f"неизвестное действие - {break_up_action}")

    def meditate(self):
        if self.strength >= MeditateParameters.STRESS_REDUCE:
            self.stress -=  MeditateParameters.STRESS_REDUCE
        else:
            self.stress = 0
        print("Вы помедитировали, успокоились, нашли просветление")

    def read(self):
        while True:
            book = input("какую книгу хотите почитать\n"
                         "фантастику        научную\n"
                         "1/2\n"
                         ":")
            if book == "1":
                self.stress -= ReadParameters.STRESS_REDUCE
                self.intelligence += ReadParameters.INTELLIGENCE_INCREASE_FANTASY
                print(f"вы почитали интересную художественную книгу, успокоились и стали чуть умнее\n"
                      f"интеллект - {self.intelligence}")
                break
            elif book == "2":
                self.intelligence += ReadParameters.INTELLIGENCE_INCREASE_SCIENCE
                print(f"вы почитали научную книгу и стали умнее\n"
                      f"интеллект - {self.intelligence}")
                break
            else:
                print(f"неизвестное действие - {book} ")
