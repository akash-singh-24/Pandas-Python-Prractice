# Rock Paper Scissor
import random
options = ['rock','paper','scissor']

user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose Rock/Paper/Scissor to Play. Q to quit from game. ").lower()
    rand_int = random.randint(0, 2)
    computer_choice = options[rand_int]
    if user_choice.lower() == 'q':
        break
    elif user_choice not in options:
        print('Cannot understand you!')
        continue
    else:
        print("Analysing")
        if user_choice == 'rock' and computer_choice == 'scissor':
            print('You Win this Round! Bravo!')
            user_score += 1
        elif user_choice == 'scissor' and computer_choice == 'paper':
            print('You Win this Round! Congo!')
            user_score += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You Win this Round! Well Done!')
            user_score += 1
        else:
            print('Computer Wins! Better Luck Next Time')
            computer_score += 1


print(f"Your Score {user_score}. Computer Score {computer_score}")