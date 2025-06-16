# Создай иерархию классов для работы с геометрическими фигурами. Все фигуры должны иметь методы для вычисления площади (area)
# и периметра (perimeter). У разных фигур эти методы реализуются по-своему — это и есть полиморфизм.
# Требования:
# 1. Базовый класс:
# Создай базовый класс Shape:
# Методы:
# area(self): возвращает площадь фигуры.
# perimeter(self): возвращает периметр фигуры.
# В базовом классе эти методы можно реализовать как заглушки, выбрасывающие NotImplementedError.

# 2. Производные классы:
# Класс Circle:
# Атрибут: radius: float
# Формулы:
# area = π * r²
# perimeter = 2 * π * r

# Класс Rectangle:
# Атрибуты: width: float, height: float
# Формулы:
# area = width * height
# perimeter = 2 * (width + height)

# Класс Triangle:
# Атрибуты: a: float, b: float, c: float (стороны треугольника)
# Формулы:
# perimeter = a + b + c
# area — по формуле Герона:
# s = (a + b + c) / 2
# area = sqrt(s * (s - a) * (s - b) * (s - c))

import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius: float):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    pass


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        # Добавьте проверку, возможно ли построить треугольник с заданными сторонами
        pass

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
