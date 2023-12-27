def mileToKm(x):
    kilometer = x * 1.609344
    return kilometer

mile = float(input())

mile_to_kilometer = mileToKm(mile)

print(f"{mile_to_kilometer}")