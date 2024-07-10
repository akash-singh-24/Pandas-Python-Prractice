import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'black', 'green', 'pink', 'cyan', 'brown', 'yellow', 'orange', 'purple']

def start_race(colors):

    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y > HEIGHT//2 - 10:
                time.sleep(3)
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.penup()
        racer.shape('turtle')
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.left(90)
        turtles.append(racer)
        time.sleep(0)
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


def get_racers():
    global racers
    while True:
        racers = input("Enter a Number of Racers (2-10) : ")
        if racers.isdigit():
            racers = int(racers)
            if racers > 1 and racers < 11:
                return racers
            else:
                print("Input Number in specified range ")
        else:
            print("Only Digit are allowed")


racers = get_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner_turtle = start_race(colors)
print(f"The winner is turtle coloured : {winner_turtle.upper()}")