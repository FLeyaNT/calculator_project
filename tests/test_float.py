import pytest

from .fixtures.fixture_calculator import calculator

from src.main import Calculator


def test_float_number(calculator: Calculator):
    calculator.number.set('175')
    calculator.setPoint()
    calculator.setPoint()
    calculator.setNum('5')
    calculator.setPoint()
    result = calculator.number.get()
    assert result == '175.5', \
        f'Ошибка в функции setPoint(): ожидалось число 175.5, а получено {result}'
