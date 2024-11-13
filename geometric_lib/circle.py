import math

from .exceptions import NotPositiveLengthException


def area(r: float) -> float:
    """Рассчитывает площадь окружности из её радиуса.

    :param r: Радиус окружности
    :return: Площадь окружности
    """
    
    if r <= 0:
        raise NotPositiveLengthException(r)

    return math.pi * r * r


def perimeter(r: float) -> float:
    """Рассчитывает периметр окружности из её радиуса.

    :param r: Радиус окружности
    :return: Периметр окружности
    """

    if r <= 0:
        raise NotPositiveLengthException(r)

    return 2 * math.pi * r

