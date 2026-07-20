# Use float(input()) to collect two numbers from the user
# Calculate and display: addition, subtraction, multiplication, division
# Calculate and display: floor division (//) and modulus (%)
# Round all results to 2 decimal places using round()
# Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
# Display all results in a formatted table using f-strings


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n".format("Operation", "Result"))
print("-" * 27)

print(f"Addition value: {round(num1 + num2):.2f} rounded")
print(f"Subtraction value: {round(num1 - num2):.2f} rounded")
print(f"Multiplication value: {round(num1 * num2):.2f} rounded")

print("-" * 27)
if abs(num2) == 0: 

    error = "A division by zero is prohibited. Try a non-zero divisor!"
    print(f"Division value: {error}")
    print(f"Flr Division value: {error}")
    print(f"Modulus value: {error}")

else:
    print(f"Division value: {round(num1 / num2):.2f} rounded")
    print(f"Flr Division value: {round(num1 // num2):.2f} rounded")
    print(f"Modulus value: {round(num1 % num2):.2f} rounded")




