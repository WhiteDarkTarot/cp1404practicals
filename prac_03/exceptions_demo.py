"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        raise ValueError("Denominator cannot be zero!")

    fraction = numerator / denominator
    print(fraction)
except ValueError as ve:
    print(ve)
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
