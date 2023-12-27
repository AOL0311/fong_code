def validTriangleSides(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False
    
def sumOdSides(x, y, z):
    return x + y + z

while True:
    num_one, num_two, num_three = map(float, input().split(" "))

    if num_one < 0 or num_two < 0 or num_three < 0:
        break

    else:
        valid_or_not = validTriangleSides(num_one, num_two, num_three)

        if valid_or_not == True:
            sum_sides = sumOdSides(num_one, num_two, num_three)

            print(f"{valid_or_not}\n{num_one} {num_two} {num_three}\n{sum_sides}")

        else:
            print(f"{valid_or_not}")