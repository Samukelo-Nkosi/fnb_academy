# challenge1 : creating The Concert Ticket Booker

#Create a program that acts as a digital ticket counter.
#1. Ask the user for their name.
#2. Ask them for the name of the band/artist they want to see.
#3. Print a personalized confirmation message using 
# an f-string that says something like: “Hey [Name]! 
# Your tickets to see [Artist] are booked successfully!”

user_name = input("1. Enter your name: ")
user_request = input("2. Which Band/Artist would you like to see at Mdu a.k.a Trp OMS? : ")

print('-' * 27)

print(f"Hey {user_name}! Your tickets to see {user_request} are booked successfully!")