def triangleArea(x, y):
    area = x * y / 2
    return area

length, height = map(float, input().split(" "))

triangle_area = triangleArea(length, height)

print(f"{triangle_area}")