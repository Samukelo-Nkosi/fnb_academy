# challenge : The High-Score Tracker Game

while True:
    score = input("Enter a game score (or type 'stop' to quit): ")
    print("-" * 67)

    if score.strip().lower() == "stop":
        print("Game session ended!")
        break

    else:
        score = input(score)

    if score > 100:
        print("Wow! That's a new high score!")

    else:
        print("Good try, keep playing!")    