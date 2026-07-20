# creating a smart atm withdrawal simulator

#   Simulate a bank transaction checking if a user has enough money.
#1. Set a fixed variable representing a bank balance, for example: balance = 500.
#2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).
#3. If the request is less than or equal to the balance, deduct the amount and print:
#   “Withdrawal successful! Remaining balance: RX”.
#4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.
#5. Otherwise (else), print: “Declined. Insufficient funds”

balance = 5000
withdrawal_amount = float(input("Enter amount to withdraw: "))
print("-" * 67)

if withdrawal_amount <= balance and withdrawal_amount > 0:

    balance -= withdrawal_amount
    print(f"Withdrawal successful!")

elif withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")

else:
        print("Declined. Insufficient funds.")


print(f"Amount withdrawn: R{round(withdrawal_amount):.2f}")
print(f"Available Balance: R{round(balance):.2f}")
