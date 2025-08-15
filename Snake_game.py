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
    cursor.penup()
    cursor.goto(i)
    segment.append(cursor)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segment)-1,0,-1):
        new_x=segment[seg_num-1].xcor()
        new_y=segment[seg_num-1].ycor()
        segment[seg_num].goto(new_x,new_y)
    segment[0].forward(20)

   
   

screen.exitonclick()