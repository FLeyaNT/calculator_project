import pytest
from src.main import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_sum_with_simple_data(calculator: Calculator):
    calculator.expression.set('100 + 20')
    calculator.getResult()
    print(calculator.number)
    assert (
        str('119') == calculator.number,
        f'Ожидалось 120, но получили {calculator.number}'
    )
