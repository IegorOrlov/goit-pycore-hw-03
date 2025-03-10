import random


def valid(min, max, quantity) -> bool:
    if min < 1:
        print("min value should be positive")
        return False
    elif max > 1000:
        print("max value should be less than 1000")
        return False
    elif max <= min:
        print("max value should be bigger than min value")
        return False
    elif quantity <= min or quantity >= max:
        print("quantity value should be between min and max values")
        return False
    return True


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if not valid(min, max, quantity):
        return None

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return sorted(numbers)


print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))
