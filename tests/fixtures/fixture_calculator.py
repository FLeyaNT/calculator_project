import pytest
from src.main import Calculator


@pytest.fixture
def calculator():
    calc = Calculator(testing_mode=True)
    return calc
