def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


celsius_temp = 30
fahrenheit_temp = 86

converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temp)
converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temp)

print(f"{celsius_temp} Celsius is equivalent to {converted_to_fahrenheit:.2f} Fahrenheit.")
print(f"{fahrenheit_temp} Fahrenheit is equivalent to {converted_to_celsius:.2f} Celsius.")
