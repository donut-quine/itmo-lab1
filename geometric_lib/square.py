from .exceptions import NotPositiveLengthException

def area(a: float) -> float:
    """Рассчитывает площадь квадрата из его стороны.

    :param a: Сторона квадрата
    :return: Площадь квадрата
    """

    if a <= 0:
        raise NotPositiveLengthException(a)

    return a * a


def perimeter(a: float) -> float:
    """Рассчитывает периметр квадрата из его стороны.

    :param a: Сторона квадрата
    :return: Периметр квадрата
    """
    
    if a <= 0:
        raise NotPositiveLengthException(a)

    return 4 * a
