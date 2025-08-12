from turtle import Screen, Turtle
import time

screen=Screen()
screen.setup(width=500,height=500)
screen.bgcolor("lightgreen")
screen.title("SNAKE GAME")
segment=[]

j=0
pos=[(0,0),(-20,0),(-40,0)]


for i in pos:
    cursor=Turtle("square")
    if j%2==0:
        cursor.color("green")
    else:
        cursor.color("black")
    j=j+1
    cursor.penup
    cursor.goto(i)
    segment.append(cursor)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)