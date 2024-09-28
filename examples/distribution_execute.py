import probabilistic
import random

def toss_coin():
    """Simulates tossing a coin."""
    return "Heads" if random.choice([True, False]) else "Tails"

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

def get_color():
    """Randomly selects a color."""
    colors = ["Red", "Blue", "Green", "Yellow"]
    return random.choice(colors)


distributions = probabilistic.distribution_execute([toss_coin, roll_dice, get_color], n=[500, 1000, 5000])

for d in distributions:
    print(d)