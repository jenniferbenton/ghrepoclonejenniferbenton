import random

list_move=("Rock" , "Paper" , "Scissors")
computer_choice=random.choice(list_move)
move=input("Enter your move ")
print(f"Your move is {move}")
print(f"Computer move is {computer_choice}")

if computer_choice == "Rock" and move == "Scissors":
    print("Computer wins!")

elif computer_choice == "Rock" and move == "Paper":
    print("You win!")

elif computer_choice == "Paper" and move == "Scissors":
    print("You win!")

elif computer_choice == "Paper" and move == "Rock":
    print("Computer wins!")

elif computer_choice == "Scissors" and move == "Paper":
    print("Computer Wins!")

elif computer_choice == "Rock" and move == "Rock":
    print("It's a tie!")

elif computer_choice == "Paper" and move == "Paper":
    print("It's a tie!")

elif computer_choice == "Scissors" and move == "Scissors":
    print("It's a tie!")
