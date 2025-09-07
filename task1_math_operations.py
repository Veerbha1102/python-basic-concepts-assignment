# task1_math_operations.py
# Author: Veer Bhanushali

# 1. Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Protect against division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# 3. Display results
print("\n--- Results ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
