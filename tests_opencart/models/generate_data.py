import random
import string


def random_data(value):
    characters = string.digits + string.ascii_lowercase
    return "".join(random.choice(characters) for i in range(value))
