import pytest

from .fixtures.fixture_calculator import calculator

from src.main import Calculator


@pytest.mark.parametrize(
    'expression, expected',
    [
        ('20 + 10', '30'),
        ('5 - 5', '0'),
        ('10.5 + 5.7', '16.2')
    ]
)
def test_sum_with_simple_data(
    calculator: Calculator, expression, expected
):
    result = str(calculator.calculate(expression))
    assert expected == result, \
        f'Ожидалось {expected}, но получили {result}'
