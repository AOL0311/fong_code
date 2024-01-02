def validTriangleSides(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False
    
def sumOfSides(x, y, z):
    return x + y + z

def main():
    while True:
        a, b, c = map(float, input().split(" "))

        if a < 0 or b < 0 or c < 0:
            break

        else:
            valid_or_not = validTriangleSides(a, b, c)

            if valid_or_not == True:
                sum_sides = sumOfSides(a, b, c)

                print(f"{valid_or_not}\n{a} {b} {c}\n{sum_sides}")
            
            else:
                print(f"{valid_or_not}")


if __name__ == "__main__":
    main()