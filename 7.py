import math

def circleArea(x):
    area = x ** 2 * math.pi
    return area

def circlePerimeter(x):
    perimeter = x * 2 * math.pi
    return perimeter

radius = float(input())

circle_area = circleArea(radius)

circle_perimater = circlePerimeter(radius)

print(f"{circle_area} {circle_perimater}")