import turtle
import time
import random
#setting up the screen
delay=0.1
s=turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)

#snake
t=turtle.Turtle()
t.speed(0)
t.shape("square")
t.color("red")
t.penup()
t.goto(0,0)
t.direction="stop"

#snake food
f=turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("blue")
f.penup()
x=random.randint(-290,290)
y=random.randint(-290,290)
f.goto(x,y)
f.direction="stop"

parts=[]

#user inputs
def go_up():
    t.direction="up"
def go_down():
    t.direction="down"
def go_left():
    t.direction="left"
def go_right():
    t.direction="right"


#functions
def move():
    if(t.direction)=="up":
        y=t.ycor()
        t.sety(y+20)
    if(t.direction)=="down":
        y=t.ycor()
        t.sety(y-20)
    if(t.direction)=="left":
        x=t.xcor()
        t.setx(x-20)
    if(t.direction)=="right":
        x=t.xcor()
        t.setx(x+20)


#listen
s.listen()
s.onkeypress(go_up,"w")
s.onkeypress(go_down,"s")
s.onkeypress(go_left,"a")
s.onkeypress(go_right,"d")

#loop
while(True):
    s.update()
    time.sleep(delay)
    if t.distance(f)<20:
        #moving food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        f.goto(x,y)

        #adding the tail effects
        n=turtle.Turtle()
        n.speed(0)
        n.shape("square")
        n.color("orange")
        n.penup()
        parts.append(n)
        
    #adding tail from backward direction
    for index in range(len(parts)-1,0,-1):
        x=parts[index-1].xcor()
        y=parts[index-1].ycor()
        parts[index].goto(x,y)
    if len(parts)>0:
        x=t.xcor()
        y=t.ycor()
        parts[0].goto(x,y)
        
    move()
    
    if(t.xcor()>295 or t.xcor()<-295 or t.ycor()>295 or t.ycor()<-295):
        time.sleep(1)
        t.goto(0,0)
        t.direction="stop"

        for i in parts:
            i.goto(1000000000000000,100000000000000)
        parts.clear()
    #body collision
    for i in parts:
        if(i.distance(t)<20):
            time.sleep(1)
            t.goto(0,0)
            t.direction="stop"

            for i in parts:
                i.goto(1000000000000000,100000000000000)
            #clearing parts again
            parts.clear()
        
    
    
        
    


