import random

random_float_0_to_1 = random.random()
print("Random float between 0 and 1:",random_float_0_to_1)

start_range, end_range = 5.0, 10.0
random_float_in_range = random.uniform(start_range, end_range)
print("Random float between",start_range,"and",end_range,":",random_float_in_range)
