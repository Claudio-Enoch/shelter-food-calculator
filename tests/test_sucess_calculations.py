import pytest


def test_generic_dog_counts(food_calculator):
    assert food_calculator(small=5, medium=3, large=7, leftover_food=17) == 363.6


def test_max_dog_count(food_calculator):
    assert food_calculator(small=10, medium=10, large=10, leftover_food=20) == 696.0


def test_max_dog_food_required(food_calculator):
    assert food_calculator(small=0, medium=0, large=30, leftover_food=0) == 1080.0


@pytest.mark.parametrize("small, medium, large, expected",
                         [
                             [5, 0, 0, 58.8],
                             [0, 5, 0, 118.8],
                             [0, 0, 5, 178.8],
                         ])
def test_single_dog_count(food_calculator, small, medium, large, expected):
    assert food_calculator(small=small, medium=medium, large=large, leftover_food=1) == expected


def test_no_leftovers(food_calculator):
    assert food_calculator(small=5, medium=5, large=5, leftover_food=0) == 360.0


def test_no_dogs_with_leftovers(food_calculator):
    assert food_calculator(small=0, medium=0, large=0, leftover_food=10) == 0.0


def test_no_dogs_with_no_leftovers(food_calculator):
    assert food_calculator(small=0, medium=0, large=0, leftover_food=0) == 0.0
