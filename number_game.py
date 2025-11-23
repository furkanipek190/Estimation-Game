# No external libs beyond stdlib
import random

print()
print("\nWelcome to the number guessing game!")
print("*" * 40)
print("I've picked a number between 1 and 100.\n")

random_number = random.randint(1, 100)
attempt = 0

while True:
    try:
        estimate = int(input("Enter your estimate: ").strip())
        # 1) Check for DECIMAL first (if 102 comes up, see that first.)
        if estimate < 1 or estimate > 100:
            print(" Please enter a number between 1 and 100!")
            continue

        attempt += 1

        # 2) Then the FORECAST vs TARGET comparison
        if estimate < random_number:
            print("Enter a larger number!")
        elif estimate > random_number:
            print("Enter a smaller number!")
        else:
            print(f" Congratulations! You found it in {attempt} tries!")
            break

    except ValueError:
        print("Please just enter numbers!")
