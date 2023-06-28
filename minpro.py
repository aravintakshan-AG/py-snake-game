from turtle import *
from random import randrange
from freegames import square,vector
from inst import *
from time import sleep
from fil import *
from __init__ import *

col,st,na,le,sp=instr()
if le==1:
    le=150
elif le==2:
    le=100
else:
    le=50

apple=vector(0,0)
snake=[vector(0,0)]
loca=vector(0,-10)
if sp==2:
    brick=[vector(10,10),vector(10,10)*5,vector(10,10)*10,vector(10,10)*15,vector(10,10)*20,vector(10,10)*25,
       vector(-10,-10),vector(-10,-10)*5,vector(-10,-10)*10,vector(-10,-10)*15,vector(-10,-10)*20,vector(-10,-10)*25,
       vector(10, -10), vector(10, -10)*5,vector(10, -10) * 10, vector(10, -10) * 15, vector(10, -10) * 20,vector(10, -10) * 25,
       vector(-10, 10), vector(-10, 10)*5,vector(-10, 10) * 10, vector(-10, 10) * 15, vector(-10, 10) * 20,vector(-10, 10) * 25
       ]
else:
    brick=[]

def re(x,y):
    loca.x=x
    loca.y=y

def ground(sn):
    return -350<sn.x<325 and -283<sn.y<280

def snake_movement():
    score=0
    sn=snake[-1].copy()
    sn.move(loca)
    if not ground(sn) or (sn in snake) or (sn in brick):
        score =(len(snake)-1)
        print("name of player =",na,"\nscore=",score,"\ngameover")
        dat(na,score)
        exit(0)
    snake.append(sn)
    if sn==apple:
        apple.x=randrange(-30,30)*10
        apple.y=randrange(-20,20)*10
        if not apple in brick:
            apple.x = randrange(-30,30) * 10
            apple.y = randrange(-20,20) * 10
        lo1=randrange(-30,30)*10
        lo2=randrange(-20,20)*10
        brick.append(vector(lo1,lo2))
    else:
        snake.pop(0)
    clear()
    for a in snake:
        square(a.x,a.y,10,col)
    square(apple.x,apple.y,10,"red")
    for b in brick:
        square(b.x,b.y,10,"blue")
    update()
    ontimer(snake_movement,le)
def ex():
    score = (len(snake) - 1)
    print("score=", score, "\ngameover")
    exit(0)


if st=="START" or st=="start":
    sleep(3)
    hideturtle()
    bgcolor("black")
    tracer(False)
    listen()
    onkey(lambda:re(10,0),"Right",)
    onkey(lambda:re(-10,0),"Left")
    onkey(lambda:re(0,10),"Up")
    onkey(lambda:re(0,-10),"Down")
    onkey(lambda:re(10,0),"d")
    onkey(lambda:re(-10,0),"a")
    onkey(lambda:re(0,10),"w")
    onkey(lambda:re(0,-10),"s")
    onkey(lambda:ex(),"q")
    snake_movement()
    done()