import pytest

from .fixtures.fixture_calculator import calculator


class TestCalculatorFunctions:
    
    @pytest.mark.parametrize(
        'input_num, expected',
        [
            # Базовые случаи
            ('16', '4'),
            ('9', '3'),
            ('0', '0'),
            ('1', '1'),
            ('2.25', '1.5'),
            ('0.25', '0.5'),
            
            # Большие числа
            ('1000000', '1000'),
            ('100000000', '10000'),
            ('999999999', '31622.7765858724'),
            ('123456789', '11111.1110605556'),
            
            # Десятичные дроби
            ('0.0001', '0.01'),
            ('0.000001', '0.001'),
            ('123.456', '11.1110755555'),
        ]
    )
    def test_square_root(self, calculator, input_num, expected):
        calculator.number = input_num
        calculator.getFunction('√')
        assert calculator.number == expected

    @pytest.mark.parametrize(
        'input_num, expected',
        [
            # Базовые случаи
            ('5', '25'),
            ('-5', '25'),
            ('0', '0'),
            ('1.5', '2.25'),
            ('10', '100'),
            ('0.5', '0.25'),
            
            # Большие числа
            ('1000', '1000000'),
            ('9999', '99980001'),
            ('1000000', '1000000000000'),
            ('12345', '152399025'),
            
            # Десятичные дроби
            ('0.01', '0.0001'),
            ('0.001', '0.000001'),
            ('123.456', '15241.383936'),
        ]
    )
    def test_power(self, calculator, input_num, expected):
        calculator.number = input_num
        calculator.getFunction('x^2')
        assert calculator.number == expected

    @pytest.mark.parametrize(
        'input_num, expected',
        [
            # Базовые случаи
            ('4', '0.25'),
            ('2', '0.5'),
            ('1', '1'),
            ('10', '0.1'),
            ('0.5', '2'),
            ('0.25', '4'),
            
            # Большие числа
            ('1000', '0.001'),
            ('1000000', '0.000001'),
            ('999999', '0.000001'),
            
            # Десятичные дроби
            ('0.1', '10'),
            ('0.01', '100'),
            ('0.001', '1000'),
            ('123.456', '0.0081000518'),

            ('0', 'Ошибка')
        ]
    )
    def test_reciprocal(self, calculator, input_num, expected):
        calculator.number = input_num
        calculator.getFunction('1/x')
        assert calculator.number == expected