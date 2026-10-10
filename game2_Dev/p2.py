# set up the screen
import turtle
import pygame
wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600) 
wn.tracer(0) 

# score
score_a=0
score_b=0

# paddle A
paddle_a=turtle.Turtle() # turtle is module name and Turtle is class name
paddle_a.speed(0)# not a spped of motion its for the animation and set to zero means max speed
paddle_a.shape("square") # builtin shapes in turtle 1:1
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # 1:5 shape
paddle_a.penup() # 
paddle_a.goto(-350,0) # set position at (-350,0)


# paddle B
paddle_b=turtle.Turtle() # turtle is module name and Turtle is class name
paddle_b.speed(0)# not a speed of motion its for the animation and set to zero means max speed //0 fastest possible//1 slower to 10 fastest 
paddle_b.shape("square") # builtin shapes in turtle 1:1
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) # 1:5 shape
paddle_b.penup() # it lifts the turtle's pen so that it doesn't draw a line when it moves.
# this is similar to lifting the human pen when drawing
# also used to move a turtle to a new location without drawing a line
# used to stop tracing the movement of turtles
# pendown() = opp of penup()
paddle_b.goto(350,0) # set position at (-350,0)

# ball
ball=turtle.Turtle() # turtle is module name and Turtle is class name
ball.speed(0)# not a spped of motion its for the animation and set to zero means max speed
ball.shape("circle") # builtin shapes in turtle 1:1
ball.color("Red")
ball.penup() # 
ball.goto(0,0) # set position at (-350,0)
ball.dx=0.15
ball.dy=0.15

# pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # hide the pen only text will seen
pen.goto(0,260)
pen.write("Player A:"+str(score_a)+" Player B:"+str(score_b),align="center",font=("font1.ttf",24,"normal"))
# pen.forward(-100) and backward  
# pen.left(10) and right
# pen.up() and  down is same as penup and pendown
# pen.shape("arrow")//blank,circle,classic,square,triangle,turtle
# pen.stamp() is used to give stamp or footprint though the pen is up and if used in loop then it will work as paint brush

# function
def paddle_a_up():
    y=paddle_a.ycor() # return y cordinate
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor() # return y cordinate
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor() # return y cordinate
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor() # return y cordinate
    y-=20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
# wn.exitonclick() # it exit on mouse click

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b-=2
        pen.clear() # clear the pen
        pen.write("Player A:"+str(score_a)+" Player B:"+str(score_b),align="center",font=("font1",24,"normal"))

    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a-=2
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("font1",24,"normal"))


    if paddle_a.ycor()>250:
        paddle_a.sety(250)
    
    if paddle_a.ycor()<-250:
        paddle_a.sety(-250)
        
    if paddle_b.ycor()>250:
        paddle_b.sety(250)
    
    if paddle_b.ycor()<-250:
        paddle_b.sety(-250)

        # paddle and ball collision
    if(ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("font1",24,"normal"))

    if(ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("font1",24,"normal"))

    

    
    # if (paddle_a.ycor()-50<=ball.ycor()<=paddle_a.ycor()+50) and (paddle_a.xcor()+10==ball.xcor()-10):
    #     ball.dx*=-1
    #     print("done")
    
    # if (paddle_b.ycor()-50<=ball.ycor()<=paddle_b.ycor()+50) and (paddle_b.xcor()-10==ball.xcor()+10):
    #     ball.dx*=-1
    #     print("done")

    # 20:20 len and wid

    # new tech to update string is 
    # str="player A={} and player B={}".format(score_a,score_b)