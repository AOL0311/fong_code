def sum(x):
    total = 0
    while x > 0:
        total += x
        x -= 1
    return total

num = int(input())

total = sum(num)

print(f"{total}")