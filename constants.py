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
    MEDIUM = 40
    HIGH = 80


class TirednessParameters(IntEnum):
    FOR_SINGLE_ACTIVE = 10
    MAXIMUM = 100

class RangParameters(IntEnum):
    MONEY_SILVER = 100
    MONEY_GOLD = 250
    MONEY_PLATINUM = 500
    MONEY_DIAMOND = 750
    MONEY_MASTER = 1000
    MONEY_GRANDMASTER = 2000