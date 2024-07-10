# Guessing the Number
import random

start_value = input("Enter the 1st Number for range Start : ")

while start_value.isdigit() == False:
    start_value = input("Incorrect Format! Please Enter the 1st Number for range Start : ")

end_value = input("Enter the 2nd Number for range Start : ")

while end_value.isdigit() == False:
    end_value = input("Incorrect Format! Please Enter the 2nd Number for Range Start : ")

while int(end_value) <= int(start_value):
    end_value = input("Negative Range! Please Enter the 2nd Number greater than Start Number : ")

rand_int = random.randint(int(start_value),int(end_value))
print(f'Random Number : {rand_int}')

guess_number = 0
cnt = 0
i = 0
keyss = 0
while True and i < (int(end_value) - int(start_value)) :
    guess_number1 = input("Guess A Number : ")
    guess_number = guess_number1
    i += 1
    if guess_number.isdigit() == False:
        cnt += 1
        continue
    elif int(guess_number) == rand_int:
        cnt += 1
        keyss = 1
        break
    else:
        cnt += 1
        print("Wrong Guess!")
        if int(guess_number) > rand_int:
            print('Wrong Guess! Actual Number is Lower than this.')
        else:
            print('Wrong Guess! Actual Number is Higher than this.')

if keyss == 1:
    print(f"Well Done! You Got the Correct Number in {cnt} times")
elif i >= (int(end_value) - int(start_value)):
    print(f"Sorry Out of Guesses")
else:
    print('Not a Correct Guess')