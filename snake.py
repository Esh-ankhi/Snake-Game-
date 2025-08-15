from turtle import Turtle
POS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()

    def create_snake(self):
        
        j=0
        for i in POS:
            cursor=Turtle("square")
            if j%2==0:
                cursor.color("green")
            else:
                cursor.color("black")
            j=j+1
            cursor.penup()
            cursor.goto(i)
            self.segment.append(cursor)

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(MOVE_DISTANCE)