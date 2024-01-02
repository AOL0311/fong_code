def sum(x):
    total = 0
    while x > 0:
        total += x
        x -= 1
    return total

def main():
    num = int(input())
    total = sum(num)
    print(f"{total}")

if __name__ == "__main__":
    main()