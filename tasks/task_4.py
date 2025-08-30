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
        """Вычисление площади фигуры"""
        pass

    @abstractmethod
    def perimeter(self):
        """Вычисление периметра фигуры"""
        pass


class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительными")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        # Проверяем условие существования треугольника:
        # сумма любых двух сторон > третьей
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2  # полупериметр
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
