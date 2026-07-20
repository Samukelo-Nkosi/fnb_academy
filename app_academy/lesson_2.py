#Tracking individual letters
name = "Samukelo"

print (name[0])
print (name[1])
print (name[2])

print (name[-3])
print (name[-2])
print (name[-1],"\n")

#using String methods
town = "  Johannesburg  "
print (town.upper())
print (town.strip())

#making a professional email generator
first_name = input("Enter your first name: ").strip()
middle_name = input ("Enter your middle name: ").strip()
last_name = input("Enter your last name: ").strip()

username = f"{first_name[0]}{middle_name[0]}{last_name}"
print (f"Your email is: {username.lower()}@university.co.za")