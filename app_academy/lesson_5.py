# a guessing game

secret_word = "python"

while True:
    user = input("Enter the programming laguage we are using: ").lower()


    if user == secret_word:
        print(f"You guessed the correct language!")
        break
    else:
        print("Incorrect guess. Try again.")