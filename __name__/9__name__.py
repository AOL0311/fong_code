import math

def abs(x):
    return math.fabs(x)

def main():
    num = float(input())
    absolute_value = abs(num)
    print(f"{absolute_value}")

if __name__ == "__main__":
    main()