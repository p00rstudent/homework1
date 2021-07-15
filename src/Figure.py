from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError('Figure class object excepted')
