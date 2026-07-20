#basic if/else statements

age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket? (Yes/No): ")

print('-' * 20)

if age >= 18 and section_pass == "Yes":
    print("Access permitted to the VIP section!")

elif age >= 18:
    print("Access permitted to the General section!")

else:
    print("Access denied!")    