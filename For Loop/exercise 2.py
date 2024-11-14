import random


def guess_game():
    computer_guess = random.choice([i for i in range(1,11)])
    print(f"Computer picked {computer_guess}")
    num_trial = 0
    while num_trial <= 5:
        user_guess = int(input(f"Please enter your guess here: "))
        if computer_guess == user_guess:
            print(f"Congratulations you guessed it right!")
            break

        elif computer_guess < user_guess:
            print(f"You have entered a number greater than the computer guess by at least {user_guess-computer_guess-1}")
            num_trial +=1
            continue
        elif computer_guess > user_guess:
            print (f"You have entered a number less than the computer guess by at least{computer_guess-user_guess - 1}")
            num_trial +=1
            continue

