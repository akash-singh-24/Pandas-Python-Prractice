import random
player_master_score = [0 for _ in range(0,3)]

def roll():
    return random.randint(1,6)

while True:
    n = input("Enter Number of Players between 2- 4 ")
    if n.isdigit() == False:
        print("Please Enter Number between 2-4 Only")
        continue
    elif int(n) > 4 or int(n) < 2:
        print("Number of Players is Out of Range, Re - Enter Number ")
    else:
        break

max_score = 50
current_score = 0

while max(player_master_score) < max_score:
    for player_id in range(0,int(n)):
        print(f"\n Player {player_id + 1} Chance to Play. Leaderboard Score is {player_master_score[player_id]} \n")
        current_score = 0

        while True:
            should_roll = input("Want to Roll?\n (y/n) : ")
            if should_roll.lower() != 'y':
                break
            else:
                roll_value = roll()
                if roll_value == 1:
                    current_score = 0
                    print(f"You Rolled a 1. Turn Over! Your current score is {current_score}")
                    break
                else:
                    current_score += roll_value
                    print(f"You rolled a {roll_value}. Current_score is {current_score} ")
        player_master_score[player_id] += current_score
        print(f"Overall Score of Player {player_id + 1} is {player_master_score[player_id]}")

max_score = max(player_master_score)
player_index = player_master_score.index(max_score)

print(f"\n\n WINNER!\n\n")
print(f"Player {player_index + 1} won the Game. He Scored {player_master_score[player_index]}")