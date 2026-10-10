# place a player into the screen
import pygame

# initialize the pygame
pygame.init()

# create the screen
screen=pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# Title 
pygame.display.set_caption("Space Invaders")
# icon
icon=pygame.image.load('p2.png')
pygame.display.set_icon(icon)
# background
screen.fill((200,30,60,50))# rgba value 0 to 255
pygame.display.update()# to update the display window
pygame.time.wait(1000)

#  player
playerImg=pygame.image.load('p3.png')
playerX=370
playerY=480

def player():
    screen.blit(playerImg,(playerX,playerY)) # to draw img into scree


running=True
while running:
    # screen.fill((30,40,50,6))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        screen.fill((30,40,50,6))
        # function should be after filling the background
        player()
        pygame.display.update()
# game code here