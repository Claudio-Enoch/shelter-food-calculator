import pytest


@pytest.mark.parametrize("small, medium, large",
                         [
                             [-5, 0, 0],
                             [0, -5, 0],
                             [0, 0, -5],
                             [5, 5, -1],
                         ])
def test_negative_dog_count(food_calculator, small, medium, large):
    with pytest.raises(ValueError, match="equal to or greater than 0"):
        food_calculator(small=small, medium=medium, large=large, leftover_food=1)


def test_negative_leftovers(food_calculator):
    with pytest.raises(ValueError, match="equal to or greater than 0"):
        food_calculator(small=10, medium=10, large=5, leftover_food=-5)


@pytest.mark.parametrize("small, medium, large",
                         [
                             ["4", 5, 5],
                             [5, (5,), 5],
                             [5, 5, None],
                             [5, 5, [4]],
                         ])
def test_malformed_dog_count_input(food_calculator, small, medium, large):
    with pytest.raises(TypeError, match="must be of type int"):
        food_calculator(small=small, medium=medium, large=large, leftover_food=1)


@pytest.mark.parametrize("leftover_food", ["5", (5,), None, [5]])
def test_malformed_leftover_input(food_calculator, leftover_food):
    with pytest.raises(TypeError, match="must be a float or int"):
        food_calculator(small=10, medium=10, large=5, leftover_food=leftover_food)


def test_exceeding_shelter_dog_limit(food_calculator):
    with pytest.raises(ValueError, match="dog count is limited"):
        food_calculator(small=11, medium=10, large=10, leftover_food=5)
