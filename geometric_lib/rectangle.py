from .exceptions import NotPositiveLengthException

def area(a: float, b: float) -> float:
    """Рассчитывает площадь прямоугольника из его сторон.

    :param a: 1ая сторона прямоугольника
    :param b: 2ая сторона прямоугольника
    :return: Площадь прямоугольника
    """

    if a <= 0:
        raise NotPositiveLengthException(a)
    if b <= 0:
        raise NotPositiveLengthException(b)

    return a * b


def perimeter(a: float, b: float) -> float:
    """Рассчитывает периметр прямоугольника из его сторон.

    :param a: 1ая сторона прямоугольника
    :param b: 2ая сторона прямоугольника
    :return: Периметр прямоугольника
    """

    if a <= 0:
        raise NotPositiveLengthException(a)
    if b <= 0:
        raise NotPositiveLengthException(b)

    return (a + b) * 2
