# event to control the player
import pygame

pygame.init()

screen=pygame.display.set_mode((1820,1100))

clock = pygame.time.Clock() 

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('p2.png')
pygame.display.set_icon(icon)
screen.fill((200,30,60,50))
pygame.display.update()

pygame.time.wait(1000)

playerImg=pygame.image.load('p3.png')
playerX=855
playerY=965

playerX_change=0
playerY_change=0

def player(x,y):
    screen.blit(playerImg,(x,y)) 

running=True

while running:
    screen.fill((30,40,50,6))
    if pygame.time.get_ticks()==60000: 
        running=False

    # if playerY>380:
    #     playerY-=0.1
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left key is pressed")
                playerX_change=-0.5
            if event.key==pygame.K_RIGHT:
                print("right key is pressed")
                playerX_change=0.5
            if event.key==pygame.K_UP:
                print("up key is pressed")
                playerY_change=-0.5
            if event.key==pygame.K_DOWN:
                print("down key is pressed")
                playerY_change=0.5
            if event.key==pygame.K_SPACE:
                print("space key is pressed")
                playerY_change=0
                playerX_change=0
            if event.key==pygame.K_RETURN:
                print("x:"+str(playerX)+"\nY:"+str(playerY))

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                print("key is released")
                playerX_change=0
                playerY_change=0

    if (playerX>=0 and playerX<=1720) and (playerY>=700 and playerY<=1000):
        playerX+=playerX_change
        playerY+=playerY_change
        player(playerX,playerY)
    else:
        playerX+=0
        playerY+=0
        player(playerX,playerY)
        if (playerX>1720 or playerX<0):
            if playerX>1720:
                playerX-=0.2
            else:
                playerX+=0.2
        if (playerY>1000 or playerY<700):
            if playerY>1000:
                playerY-=0.2
            else:
                playerY+=0.2

# here the picture of spaceship is not moving the new picture is created adjecent to it in very small duration seems as the moving
    pygame.display.update()
