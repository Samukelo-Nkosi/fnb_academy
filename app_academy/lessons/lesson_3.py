#Adding two numbers
#Strings
num1 = input("Enter the first number: ")
num2 = input("Enter the second number")

#Making use of type casting
print (int(num1) + int(num2))


#Restaurant simulator
bill = float(input("Enter the bill: R"))
tip = 0.15 #Float

val_tip = bill * tip
total = bill + val_tip

print (f"Here is the tip: R{val_tip}")
print (f"Here is the tip rounded: R{round(val_tip, 2)} \n")
print (f"Here is the total amount: R{total}")
print (f"Here is the total amount rounded: R{round(total)}")