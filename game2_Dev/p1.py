import turtle # used for graphics and GUI
import pygame
wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600) # here center of screen is the (0,0) so as left and right most is -400 and 400
wn.tracer(0) #stops the window from updating so that manual update and so that fast execution


# main game loop
while True:
    wn.update()