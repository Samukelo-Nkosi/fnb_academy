

first_name = input('Enter your first name: ').strip()
surname = input('Enter your surname: ').strip()
age = int(input('Enter your age: '))
favourite_number = float(input('Enter your favourite number: '))

print(f"Welcome, {first_name} {surname}!")

full_name = f"{first_name} {surname}"
print(full_name.upper())
print(full_name.title())

age_in_months = age * 12
print(f"Your age in months is {age_in_months}.")

rounded_number = round(favourite_number, 2)
print(f"Your favourite number rounded to 2 decimal places is {rounded_number:.2f}.")

print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourite_number))

