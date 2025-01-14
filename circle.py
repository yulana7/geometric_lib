import math


def area(r):
    '''принимает число r(радиус окружности), возвращает площадь окружности
    
    area(3)

    >>> 28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    '''принимает число r(радиус окружности), возвращает периметр окружности
    
    perimeter(4)

    >>> 25.132741228718345
    '''
    return 2 * math.pi * r
