# challenge2 : The Secure Password Hint Tool

# Users often forget their passwords. 
# Create a script that helps them by showing a secure hint.
#1. Ask the user to input their secret password.
#2. Use .strip() to clean up any accidental spaces they might have
#  typed at the start or end.
#3. Grab the very first letter and the very last letter of the 
# password using string indexing.
#4. Print a hint using an f-string that forces the letters into uppercase 
# so they stand out. (e.g., “Your password hint: It starts with P and ends with N”).

user_pass = input("Type your secret password to unlock: ".strip())
print('-' * 30)

first_case = user_pass[0]
last_case = user_pass[-1]

print(f"hint: It starts with{first_case.upper()} and ends with {last_case.upper()}")