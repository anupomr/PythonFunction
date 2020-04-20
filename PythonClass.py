import random
from pathlib import Path

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(0, 6)
        return first, second

dice = Dice()
print(dice.roll())


path = Path("ecommerce")
print(path.exists())

path = Path()
for file in path.glob('*.py'):
    print(file)