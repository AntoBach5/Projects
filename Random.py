import random, time

options = ["rock", "paper", "scissors"]
computer_enter = random.choice(options)

machine_counter = 0
user_counter = 0

while True:
    user_enter = input("\nEnter (rock/paper/scissors): ")
    if user_enter == computer_enter:
        print("Its a tie!")
        machine_counter += 1
        user_counter += 1
        print(f"Computer score = {machine_counter}")
        print(f"User score = {user_counter}")
    elif user_enter.lower() == "rock":
        if computer_enter == "scissors":
            print("You win! Rock beats scissors.")
            user_counter += 1
        else:
            print("You lose! Paper beats rock.")
            machine_counter += 1
        print(f"Computer score = {machine_counter}")
        print(f"User score = {user_counter}")
    elif user_enter.lower() == "paper":
        if computer_enter == "rock":
            print("You win! Paper beats rock.")
            user_counter += 1
        else:
            print("You lose! Scissors beats paper.")
            machine_counter += 1
        print(f"Computer score = {machine_counter}")
        print(f"User score = {user_counter}")
    elif user_enter.lower() == "scissors":
        if computer_enter == "paper":
            print("You win! Scissors beats paper.")
            user_counter += 1
        else:
            print("You lose! Rock beats scissors.")
            machine_counter += 1
        print(f"Computer score = {machine_counter}")
        print(f"User score = {user_counter}")
    else:
        print("That is not a valid input, try again")
    
    if machine_counter == 3 or user_counter == 3:
        break

if machine_counter == 3:
    winner = "Computer"
else:
    winner = "User"
print("The game is over!, the winner is... (DRUM ROLL!!!)")
time.sleep(1)
print(f"\nThe {winner}")
if winner == "User":
    print("Congratulations")