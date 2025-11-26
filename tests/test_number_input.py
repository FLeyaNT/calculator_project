import pytest

from .fixtures.fixture_calculator import calculator


class TestCalculatorNumber:
    
    @pytest.mark.parametrize(
        'initial, inputs, expected',
        [
            # Последовательный ввод
            ('0', ['1', '2', '3'], '123'),
            ('999', ['9'], '9999'),
            ('0', ['0', '0', '1'], '1'),
            ('-5', ['0', '0'], '-500'),
            
            # Большие числа
            ('1000000', ['0'], '10000000'),
            ('999999999', ['9'], '9999999999'),
        ]
    )
    def test_multiple_number_inputs(self, calculator, initial, inputs, expected):
        calculator.number = initial
        calculator.first_dig = (initial == '0')
        for num in inputs:
            calculator.setNum(num)
        assert calculator.number == expected

    @pytest.mark.parametrize(
        'initial, expected_after_delete',
        [
            ('123456789', '12345678'),
            ('12345678', '1234567'),
            ('1234567', '123456'),
            ('1000000', '100000'),
            ('999999999', '99999999'),
            ('0.12345', '0.1234'),
            ('-12345', '-1234'),
            ('-5', '0'),
            ('0', '0')
        ]
    )
    def test_multiple_deletions(self, calculator, initial, expected_after_delete):
        calculator.number = initial
        calculator.delDigit()
        assert calculator.number == expected_after_delete