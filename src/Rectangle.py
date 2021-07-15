from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, name: str, a: float, b: float):
        super().__init__(name)
        self.a = a
        self.b = b

    @property
    def area(self) -> float:
        return self.a * self.b

    @property
    def perimeter(self) -> float:
        return (self.a + self.b) * 2
