def mileToKm(x):
    kilometer = x * 1.609344
    return kilometer

def main():
    mile = float(input())
    mile_to_kilometer = mileToKm(mile)
    print(f"{mile_to_kilometer}")

if __name__ == "__main__":
    main()