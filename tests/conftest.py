import pytest
from food_calculator import calculate_dog_food


@pytest.fixture
def food_calculator():
    """
    Completely unneeded fixture, here just to demonstrate conftest.py usage.
    Potential functionality could be logging or timing the function.
    """
    return calculate_dog_food
