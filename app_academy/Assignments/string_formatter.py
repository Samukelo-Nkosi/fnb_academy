first_name = input('Enter your name: ').strip()
last_name = input('Enter your last name: ').strip()
your_bio = input('Enter bio message: ')

username = (f" {first_name[0]} + {last_name}").lower()
full_name = (f"{first_name} {last_name}").title()
your_bio = your_bio.strip()

user_bio = your_bio.strip().replace("I am", "I'm")

print(f"{first_name}")
print(f"{last_name}")
print(f"{your_bio}")
print(f"{len(user_bio)} characters")
