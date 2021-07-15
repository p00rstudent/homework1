import pytest

from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_triangle_creation():
    assert Triangle(name='triangle', a=1, b=1, c=100) is None


def test_triangle_creation2():
    assert Triangle(name='triangle', a=-3, b=4, c=5) is None


def test_triangle_area():
    assert Triangle(name='triangle', a=13, b=14, c=15).area == 84


def test_triangle_perimeter():
    assert Triangle(name='triangle', a=13, b=14, c=15).perimeter == 42


def test_triangle_name():
    assert Triangle(name='triangle', a=13, b=14, c=15).name == 'triangle'


def test_square_area():
    assert Square(name='square', a=10).area == 100


def test_square_perimeter():
    assert Square(name='square', a=13).perimeter == 52


def test_square_name():
    assert Square(name='square', a=13).name == 'square'


def test_rectangle_area():
    assert Rectangle(name='rectangle', a=10, b=10).area == 100


def test_rectangle_perimeter():
    assert Rectangle(name='rectangle', a=13, b=10).perimeter == 52


def test_rectangle_name():
    assert Rectangle(name='rectangle', a=13, b=10).name == 'rectangle'


def test_area_sum():
    assert Square(name='square', a=13).add_area(Rectangle(name='rectangle', a=13, b=10)) == 299


def test_area_sum_exception():
    with pytest.raises(ValueError):
        assert Square(name='square', a=13).add_area(5)


def test_area_sum_exception2():
    with pytest.raises(ValueError):
        assert Square(name='square', a=13).add_area('hello')


def test_figure_creation():
    with pytest.raises(TypeError):
        Figure(name='figure')
