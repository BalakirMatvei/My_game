from enum import Enum


class IntEnum(int, Enum):
    pass


class WorkParameters(IntEnum):
    MINIMUM_FULLNESS = 20
    MINIMUM_HEALTH = 20
    REDUCE_FULLNESS = 10
    REDUCE_HEALTH = 20


class IntelligenceLVL(IntEnum):
    MEDIUM = 100
    HIGH = 200
    VERY_HIGH = 300
    EXTRA_HIGH = 500


class EatParameters(IntEnum):
    MAXIMUM_FULLNESS = 100
    MINIMUM_FOOD = 10
    INCREASE_FULLNESS = 10
    REDUCE_FOOD = 10


class ShoppingParameters(IntEnum):
    MINIMUM_MONEY = 10
    INCREASE_FOOD = 10
    REDUCE_MONEY = 10


class GymParameters(IntEnum):
    MINIMUM_FULLNESS = 30
    INCREASE_STRENGTH = 10
    REDUCE_FULLNESS = 20


class StudyParameters(IntEnum):
    MINIMUM_FULLNESS = 10
    MINIMUM_HEALTH = 20
    INCREASE_INTELLIGENCE = 10
    REDUCE_FULLNESS = 10
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

GIFT_MONEY = 100