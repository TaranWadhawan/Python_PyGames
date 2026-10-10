# add enemy and bullets
import pygame
from moviepy.editor import VideoFileClip
import random

pygame.init()
screen=pygame.display.set_mode((1820,1100))

clock = pygame.time.Clock() 

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('p2.png')
pygame.display.set_icon(icon)
intro=pygame.image.load('intro.png')
screen.blit(intro,(-5,0))
pygame.display.update()
pygame.time.wait(500)

def intro():
    running2=True
    while running2:
        background=pygame.Surface((1820,1100))
        screen.blit(background,(0,0))
        pygame.display.update()

        clip = VideoFileClip("intro.mkv")
        clip = clip.resize(height=1100)  # Resize the video to fit the screen

        # Play the video
        for frame in clip.iter_frames(fps=30, dtype="uint8"):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        clip.close()
                        print("XXXXXXX")

            surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            screen.blit(surface, (0, 0))
            pygame.display.update()
            pygame.time.Clock().tick(30)
        
        clip.close()
        
        x=game()
        if x==False:
            running2=False



def game():

    playerImg=pygame.image.load('p3.png')
    playerX=855
    playerY=965
    playerX_change=0
    playerY_change=0

    def player(x,y):
        screen.blit(playerImg,(x,y)) 



    enemyImg=pygame.image.load('monster (1).png')
    enemyX=random.randint(0,1756)
    enemyY=0
    enemyX_change=0.3
    enemyY_change=0

    def enemy(x,y):
        screen.blit(enemyImg,(x,y)) 



    bulletImg=pygame.image.load('bullet.png')
    bulletX=playerX
    bulletY=playerY
    bulletY_change=0

    def bullet(x,y):
        screen.blit(bulletImg,(x,y)) 


    x=False
    running=True

    while running:
        screen.fill((30,40,50,6))

        if pygame.time.get_ticks()==60000: 
            running=False
            
        if enemyX<=0:
            enemyX_change=0.6
            enemyY_change=60
        elif enemyX>=1756:
            enemyX_change=-0.6
            enemyY_change=60
        else:
            enemyY_change=0
        enemyX+=enemyX_change
        enemyY+=enemyY_change 
        enemy(enemyX,enemyY)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    print("left key is pressed")
                    playerX_change=-1
                if event.key==pygame.K_RIGHT:
                    print("right key is pressed")
                    playerX_change=1
                if event.key==pygame.K_UP:
                    print("up key is pressed")
                    playerY_change=-1
                if event.key==pygame.K_DOWN:
                    print("down key is pressed")
                    playerY_change=1
                if event.key==pygame.K_SPACE:
                    print("space key is pressed")
                    playerX=855
                    playerY=965
                if event.key==pygame.K_RETURN:
                    x=True
                    bullet(bulletX,bulletY)

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    print("key is released")
                    playerX_change=0
                    playerY_change=0
                # if event.key==K_ESCAPE: 


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


        pygame.display.update()
    return running



# ////////////////////////////////////////////////////////
intro()