import math

def find_max(x, y):
    return max(x, y)

def main():
    num_one, num_two = map(float, input().split(" "))
    max_value = find_max(num_one, num_two)
    print(f"{max_value}")

if __name__ == "__main__":
    main()