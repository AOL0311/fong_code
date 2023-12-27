def fahToCel(x):
    celsius = (x - 32) / 9 * 5
    return celsius

fahrenheit = float(input())

fahrenheit_to_celsius = fahToCel(fahrenheit)

print(f"{fahrenheit_to_celsius}")