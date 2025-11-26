import pytest
from src.logic import CalculatorLogic


@pytest.fixture
def calculator():
    calc = CalculatorLogic()
    return calc
