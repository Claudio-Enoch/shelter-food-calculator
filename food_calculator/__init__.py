from typing import Union

_FOOD_MULTIPLIER = 1.2
_SMALL_MULTIPLIER = 10
_MEDIUM_MULTIPLIER = 20
_LARGE_MULTIPLIER = 30
_SHELTER_DOG_LIMIT = 30


def calculate_dog_food(small: int, medium: int, large: int, leftover_food: Union[int, float]) -> float:
    """Return amount of food to order given the number of dogs and leftovers."""
    dogs = [small, medium, large]
    # parameter type checks and validations
    if not all(isinstance(dog, int) for dog in dogs):
        raise TypeError("small, medium, and large dog values must be of type int")
    if not isinstance(leftover_food, (int, float)):
        raise TypeError("leftover food must be a float or int")
    if [dog for dog in dogs if dog < 0] or leftover_food < 0:
        raise ValueError("dog count and leftover food must have values equal to or greater than 0")
    if (total_dogs := sum(dogs)) > _SHELTER_DOG_LIMIT:
        raise ValueError(f"total dog count is limited to {_SHELTER_DOG_LIMIT}, currently at {total_dogs}")

    # calculate food required
    minimum_dog_food = small * _SMALL_MULTIPLIER + medium * _MEDIUM_MULTIPLIER + large * _LARGE_MULTIPLIER
    minimum_dog_food = (minimum_dog_food - leftover_food) if minimum_dog_food > leftover_food else 0
    required_dog_food = round(minimum_dog_food * _FOOD_MULTIPLIER, 2)
    return required_dog_food
