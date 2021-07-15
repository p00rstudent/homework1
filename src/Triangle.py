from math import sqrt

from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, name: str, a: float, b: float, c: float):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def __new__(cls, name: str, a: float, b: float, c: float):
        if not cls.is_valid(a, b, c):
            return None
        else:
            return super().__new__(cls)

    @staticmethod
    def is_valid(a: float, b: float, c: float) -> bool:
        return True if all((a > 0, b > 0, c > 0, (a + b) > c, (b + c) > a, (c + a) > b)) else False

    @property
    def area(self) -> float:
        half_p = self.perimeter / 2
        return sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c


