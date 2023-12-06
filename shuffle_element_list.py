import random

original_list = [1, 'apple', 3.14, 'banana', 42, 'orange']

shuffled_list = random.sample(original_list, len(original_list))

print("Original list:", original_list)
print("Shuffled list:", shuffled_list)
