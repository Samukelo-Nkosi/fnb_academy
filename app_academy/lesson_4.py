#Basic if/else statements
age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket? (yes/no)").lower()

if age >= 18 and section_pass == "yes":
    print("Access Granted to VIP Section !")
elif age >= 18:
    print("Access Granted to General Section !")
else:
    print("Access Denied !!!")