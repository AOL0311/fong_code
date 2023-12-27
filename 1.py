import math

def find_max(x, y):
    return max(x, y)

num_one, num_two = map(float, input().split(" "))

max_value = find_max(num_one, num_two)

print(f"{max_value}")