def rectangularArea(x, y):
    area = x * y
    return area

def retangularPerimeter(x, y):
    perimeter = (x + y) * 2
    return perimeter

def main():
    length, width = map(float, input().split(" "))
    rectangular_area = rectangularArea(length, width)
    rectangular_perimater = retangularPerimeter(length, width)
    print(f"{rectangular_area} {rectangular_perimater}")

if __name__ == "__main__":
    main()