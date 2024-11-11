import random
print("\nRock Paper and Scissors game!")
print("-----------------------------\n")
Choice_list=["Rock", "Paper", "Scissors"]

while(True):
    your_choice = input("Please enter your choice (Rock,Paper,Scissors):")
    while your_choice not in Choice_list:
        print("Invalid input try again...\n")
        your_choice = input("Please enter your choice (Rock,Paper,Scissors):")

    computer_choice = random.choice(Choice_list)
    print(f"The computer chose - {computer_choice}")
    if (your_choice=="Rock" and computer_choice=="Scissors") or (your_choice=="Scissors" and computer_choice=="Paper") or (your_choice=="Paper" and computer_choice=="Rock"):
        print("You won!")
        break
    elif (computer_choice=="Rock" and your_choice=="Scissors") or (computer_choice=="Scissors" and your_choice=="Paper") or (computer_choice=="Paper" and your_choice=="Rock"):
        print("You lose! try again...\n")
        continue
    else:
        print("it's a draw! try again...\n")
        continue
        