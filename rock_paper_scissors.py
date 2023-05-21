import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______) 
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


entry_command = input("Do you want to play - (yes) or (no): ")
my_list = ["rock", "paper", "scissors"]
wins = 0
lose = 0
while True:
    if entry_command == "yes" or entry_command == "no":
        while entry_command != "no":

            player_choice = input("What is your choice - rock, paper or scissors: ")
            computer_choice = random.choice(my_list)
            if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
                if player_choice == "rock":
                    print(rock)
                    if computer_choice == "rock":
                        print(f"Computer choice is: {computer_choice}.")
                        print(rock)
                        print("Equality, try again!")
                    elif computer_choice == "paper":
                        lose += 1
                        print(f"Computer choice is: {computer_choice}.")
                        print(paper)
                        print("Sorry, you lose!")
                    elif computer_choice == "scissors":
                        wins += 1
                        print(f"Computer choice is: {computer_choice}.")
                        print(scissors)
                        print("Well done, you won!")

                elif player_choice == "paper":
                    print(paper)
                    if computer_choice == "rock":
                        wins += 1
                        print(f"Computer choice is: {computer_choice}.")
                        print(rock)
                        print("Well done, you won!")
                    elif computer_choice == "paper":
                        print(f"Computer choice is: {computer_choice}.")
                        print(paper)
                        print("Equality, try again!")
                    elif computer_choice == "scissors":
                        lose += 1
                        print(f"Computer choice is: {computer_choice}.")
                        print(scissors)
                        print("Sorry, you lose!")

                elif player_choice == "scissors":
                    print(scissors)
                    if computer_choice == "rock":
                        lose += 1
                        print(f"Computer choice is: {computer_choice}.")
                        print(rock)
                        print("Sorry, you lose!")
                    elif computer_choice == "paper":
                        wins += 1
                        print(f"Computer choice is: {computer_choice}.")
                        print(paper)
                        print("Well done, you won!")
                    elif computer_choice == "scissors":
                        print(f"Computer choice is: {computer_choice}.")
                        print(scissors)
                        print("Equality, try again!")

                print(f"You have {wins} wins, and {lose} lose.")
                entry_command = input("Do you want to play again - (yes) or (no): ")
                if entry_command != "yes" or entry_command != "no":
                    print("Invalid input")
                    entry_command = input("Do you want to play again - (yes) or (no): ")
                if entry_command == "no":
                    print("Goodbye!")
            else:
                print("Invalid input")
                entry_command = input("Do you want to play again - (yes) or (no): ")
                if entry_command != "yes" or entry_command != "no":
                    print("Invalid input")
                if entry_command == "no":
                    print("Goodbye!")
    elif entry_command == "no":
        print("Goodbye!")

    else:
        print("Invalid input")
        entry_command = input("Do you want to play - (yes) or (no): ")


