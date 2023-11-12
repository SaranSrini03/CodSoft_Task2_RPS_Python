import random
options = ["rock", "paper", "scissors"]
running = True
winScore = 0
losingScore = 0
score = 0
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice [rock, paper, scissors] : ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        print()
    elif player == "rock" and computer == "scissors":
        print("You win!")
        print()
        score +=1
        winScore += 1

    elif player == "paper" and computer == "rock":
        print("You win!")
        print()
        score +=1
        winScore += 1

    elif player == "scissors" and computer == "paper":
        print("You win!")
        print()
        score +=1
        winScore += 1

    else:
        print("You lose!")
        print()
        score = 0
        losingScore +=1

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print(f"Your winning streak : {score}")
print(f"winning score : {winScore}")
print(f"losing score : {losingScore}")