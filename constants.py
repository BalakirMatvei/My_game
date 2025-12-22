from enum import Enum


class IntEnum(int, Enum):
    pass

class WorkParameters(IntEnum):
    MINIMUM_FULLNESS = 30
    MINIMUM_HEALTH = 30
    REDUCE_FULLNESS = 30
    REDUCE_HEALTH = 20

class IntelligenceLVL(IntEnum):
    MEDIUM = 100
    HIGH = 200
    VERY_HIGH = 300
    EXTRA_HIGH = 500

class EatParameters(IntEnum):
    MAXIMUM_FULLNESS = 100
    MINIMUM_FOOD = 10
    INCREASE_FULLNESS = 30
    REDUCE_FOOD = 20

class ShoppingParameters(IntEnum):
    MINIMUM_MONEY = 10
    INCREASE_FOOD = 10
    REDUCE_MONEY = 10

class GymParameters(IntEnum):
    MINIMUM_FULLNESS = 30
    INCREASE_STRENGTH = 10
    REDUCE_FULLNESS = 20

class StudyParameters(IntEnum):
    MINIMUM_FULLNESS = 30
    MINIMUM_HEALTH = 30
    INCREASE_INTELLIGENCE = 10
    REDUCE_FULLNESS = 30
    REDUCE_HEALTH = 20

class SleepParameters(IntEnum):
    MAXIMUM_HEALTH = 100
    MINIMUM_FULLNESS = 20
    INCREASE_HEALTH = 20
    REDUCE_FULLNESS = 10
    REDUCE_HEALTH = 50

class SalaryParameters(IntEnum):
    MINIMUM = 20
    MEDIUM = 50
    HIGH = 100
    VERY_HIGH = 150
    EXTRA_HIGH = 250

class TirednessParameters(IntEnum):
    FOR_SINGLE_ACTIVE = 10
    MAXIMUM = 100

class RangParameters(IntEnum):
    MONEY_SILVER = 100
    MONEY_GOLD = 500
    MONEY_PLATINUM = 1000
    MONEY_DIAMOND = 5000
    MONEY_MASTER = 10000
    MONEY_GRANDMASTER = 25000
    MONEY_LORD = 50000

class HealParameters(IntEnum):
    HEALTH_INCREASE = 30
    MONEY_REDUCE = 50

class AgeParameters(IntEnum):
    ADULT = 35
    OLD = 60
    LIMITATION_STRENGTH_ADULT = 8
    LIMITATION_STRENGTH_OLD = 5
    REDUCE_FULLNESS_ADULTS = 15
    REDUCE_FULLNESS_OLDS = 25

BD_GIFT_MONEY = 100

class FightParameters(IntEnum):
    MINIMUM_STRENGTH = 200
    STRENGTH_INCREASED_CHANCE = 350
    MINIMUM_FULLNESS = 60
    FULLNESS_REDUCE = 50
    HEALTH_REDUCE_WIN = 10
    HEALTH_AFTER_LOOS = 20
    DEFAULT_WIN_CHANCE = 50
    INCREASED_WIN_CHANCE = 75
    MONEY_WIN = 500
    MONEY_LOOS = 200
    STRESS_LOOS = 15

class StressParameters(IntEnum):
    STRESS_INCREASE = 10
    STRESS_REDUCE = 10
    MAXIMUM = 100
    HEALTH_REDUCE = 5

class CookingParameters(IntEnum):
    FULLNESS_INCREASE = 40
    STRESS_REDUCE = 20

class InvestParameters(IntEnum):
    MINIMUM_DEPOSIT = 100
    CHANCE = 30

BJ_Points = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 2,
    'Q': 3,
    'K': 4,
    'A': 11
}

BJ_Cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]

class ROULETTE:
    all_bets = list(str(i) for i in range(1, 37)) + ['1st 12', '2nd 12', '3rd 12', '1-18', '19-36', 'red', 'black', 'EVEN', 'ODD']

    all_results = list(str(i) for i in range(1, 37))

    black = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']

    red = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']

    even = [i for i in range(2, 37) if i % 2 == 0]

    odd = [i for i in range(1, 37) if i % 2 != 0]

    first_12 = list(str(i) for i in range(1, 13))

    second_12 = list(str(i) for i in range(13, 25))

    third_12 = list(str(i) for i in range(25, 37))

    first_half = list(str(i) for i in range(1, 19))

    second_half = list(str(i) for i in range(19, 37))

    bet_variants = {
        '1st 12': "first_12",
        '2nd 12': "second_12",
        '3nd 12': 'third_12',
        '1-18': 'first_half',
        '19-36': 'second_half',
        'EVEN': 'even',
        "ODD": 'odd',
        'red': 'red',
        'black': 'black'
    }

    colors = {
        0: 'green',
        **{str(i): 'red' for i in red},
        **{str(i): 'black' for i in black},
    }

    num_multiplier = 36
    multipliers = {
        '1st 12': 3,
        '2nd 12': 3,
        '3nd 12': 3,
        '1-18': 2,
        '19-36': 2,
        'EVEN': 2,
        "ODD": 2,
        'red': 2,
        'black': 2
    }

class DateParameters:
    MINIMUM_RATE = 7
    MAXIMUM_RATE = 10
    AVERAGE_RATE = 9
    CHANCE_UP_FOR_SELF = 10
    CHANCE_DOWN_FOR_SELF = 20
    STRENGTH_UP_CHANCE = 150
    MONEY_UP_CHANCE = 1000
    INTELLIGENCE_UP_CHANCE = 150
    INTELLIGENCE_TALK = 100
    NOT_TALK_CHANCE_DECREASE = 20
    TALK_CHANCE_INCREASE = 10
    NOT_TALK_INCREASE = 40
    MINIMUM_MONEY = 200
    MINIMUM_GIRL_CHANCE = 20
    AVERAGE_GIRL_CHANCE = 30
    MAXIMUM_GIRL_CHANCE = 40
    location_chance = {
        '1' : 0,
        '2' : 10,
        '3' : 20,
    }
    location_action = {
        '1' : 'гулять по парку',
        '2' : 'в кафе',
        '3' : 'в ресторан',
    }
    phrase_variants = {
        '1' : 'не переживай, я при бабках',
        '2' : 'на жизнь хватает',
        '3' : 'пока на мели',
    }
    location_money = {
        '1' : 0,
        '2' : 150,
        '3' : 300,
    }