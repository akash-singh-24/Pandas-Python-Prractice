# Question and Answer
from Project1_Questions import Question

print("welcome to my Game! ")

play = input("Do You want to play ? ")

if play.lower() != 'yes':
    quit()

print("Lets Play!!")

question_promt = [
    "What color apples? \n (a) Red/Green \n (b) Purple \n (c) Orange\n\n",
    "What color Banana? \n (a) Red \n (b) Yellow \n (c) Orange\n\n",
    "What color Guava? \n (a) Red \n (b) Purple \n (c) Green\n\n",
]

questions = [
            Question(question_promt[0],"a"),
            Question(question_promt[1],"b"),
            Question(question_promt[2],"c")
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You Got {score} / 3")

run_test(questions)