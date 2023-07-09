import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=550,height=500)
screen.bgcolor("light blue")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
pen = turtle.Turtle()
pen.penup() 
pen.goto(-230,200)
pen.pendown()

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

for i in range(1,11):
   pen.hideturtle()
   pen.write(i)
   pen.setheading(-90)
   pen.forward(400)
   if i==10:
       pen.write(" FINISH")
   pen.back(400)
   pen.penup()
   pen.setheading(0)
   pen.forward(50)
   pen.down()


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner! ")

            else:
                print(f"You have lost! The {winning_color} turtle is the winner! ")




        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()