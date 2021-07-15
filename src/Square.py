from src.Figure import Figure


class Square(Figure):

    def __init__(self, name: str, a: float):
        super().__init__(name)
        self.a = a

    @property
    def area(self) -> float:
        return self.a ** 2

    @property
    def perimeter(self) -> float:
        return self.a * 4
