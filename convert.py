# convert.py
# A program to convert temperature in degrees Celsius to temperature in degrees
# Fahrenheit
# From Python Programming Chapter 2


def main():
    # Input temperature in degrees C
    celsius = float(input('Enter the temperature in degrees C: '))
    # Convert using F = 9/5*C+32
    fahrenheit = 9 / 5 * celsius + 32
    # Output temperature in degrees F
    print(fahrenheit)


main()
