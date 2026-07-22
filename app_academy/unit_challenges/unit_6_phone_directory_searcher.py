# Create a mini data directory using a List and a Dictionary combined.

#1. Create a dictionary called contacts where the Keys are friend names and the Values are their phone numbers (keep phone numbers as strings so the leading 0 doesn’t drop off, e.g., “0821112222”). Fill it with 3 people.
#2. Ask the user to input the name of the friend they want to look up.
#3. Use a conditional check to see if the name matches a key. If it exists, pull out and print their number: “Found! [Name]’s number is [Number]”.
#4. Otherwise, print “Contact not found.”

contacts = {
    "Samukelo": "0692124437",
    "Anele": "0823698479",
    "Siyabonga": "0613217861",
}

name = input("Enter the name of the friend you want to look up: ")
print("----------------------------------------------------------")

if name in contacts:
    print(f"Found. {name}'s number is {contacts[name]}")

else:
    print(f"Contact not found.")    