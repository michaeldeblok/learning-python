import random
import my_module

random_integer = random.randint(1, 10)
random_float = random.random()

print(random_integer)
print(random_float)

print(my_module.pi)

randomFloat = random_float * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')