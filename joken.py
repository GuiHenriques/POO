import random

options = ["rock", "paper", "scissors"]

computer = random.choice(options)
user = input("Rock, paper or scissors? ").lower()
print(f"{user} x {computer}")

if user not in options:
    print("Invalid option")
elif computer == user:
    print("Tie")
elif (
    user == "rock" and computer == "scissors" or
    user == "paper" and computer == "rock" or
    user == "scissors" and computer == "paper"
):
    print("Win")
else:
    print("Lost")
