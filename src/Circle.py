from math import pi

from src.Figure import Figure


class Circle(Figure):

    def __init__(self, name: str, r: float):
        super().__init__(name)
        self.r = r

    @property
    def area(self) -> float:
        return pi * (self.r ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.r
