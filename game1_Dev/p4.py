# time
import pygame

# initialize the pygame
pygame.init()

# create the screen
screen=pygame.display.set_mode((800,600))
clock = pygame.time.Clock()# used to create a clock to track the time

# Title 
pygame.display.set_caption("Space Invaders")
# icon
icon=pygame.image.load('p2.png')
pygame.display.set_icon(icon)
# background
screen.fill((200,30,60,50))# rgba value 0 to 255
pygame.display.update()# to update the display window
pygame.time.wait(1000)
# pygame.time.wait and delay works same
# pygame.time.get_ticks() returns no of miliseconds until the program starts or the clock starts
# pygame.time.set_time() creates a timer event that will be posted to the event queue after a specific no of miliseconds
# pygame.time.get_fps() returns the current frame rate in frame per seconds
# clock.tick
# clock.get_time
# clock.get_rawtime
# 

#  player
playerImg=pygame.image.load('p3.png')
playerX=370
playerY=480

def player(x,y):
    screen.blit(playerImg,(x,y)) # to draw img into scree

running=True

while running:
    screen.fill((30,40,50,6))
    if playerY>380:
        playerY-=0.1
    else:
        playerX+=0.1
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    if pygame.time.get_ticks()==60000: 
        running=False
    player(playerX,playerY)
    pygame.display.update()
