import pytest

from .fixtures.fixture_calculator import calculator


class TestCalculatorPercentage:
    
    @pytest.mark.parametrize(
        'number, expected',
        [
            # Базовые проценты
            ('50', '0.5'),
            ('25', '0.25'),
            ('100', '1'),
            ('1', '0.01'),
            ('0.1', '0.001'),
            
            # Большие числа
            ('5000', '50'),
            ('1000000', '10000'),
            ('0.0001', '0.000001'),
        ]
    )
    def test_percent_basic(self, calculator, number, expected):
        calculator.number = number
        calculator.getPercent()
        assert calculator.number == expected

    @pytest.mark.parametrize(
        'expression, number, expected',
        [
            # Умножение на процент
            ('100 *', '10', '10'),
            ('200 *', '25', '50'),
            ('1000 *', '15', '150'),
            ('123.456 *', '50', '61.728'),
            
            # Сложение с процентом
            ('100 +', '10', '110'),
            ('200 +', '50', '300'),
            ('1000 +', '20', '1200'),
            
            # Вычитание процента
            ('100 -', '10', '90'),
            ('200 -', '25', '150'),
            ('1000 -', '15', '850'),
            
            # Большие числа
            ('1000000 *', '10', '100000'),
            ('5000000 +', '20', '6000000'),
            ('10000000 -', '5', '9500000'),
        ]
    )
    def test_percent_with_operations(self, calculator, expression, number, expected):
        calculator.expression = expression
        calculator.number = number
        calculator.getPercent()
        assert calculator.number == expected