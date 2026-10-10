import pygame
from moviepy.editor import VideoFileClip
import random
import time

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1820,1100))

clock = pygame.time.Clock() 

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('p2.png')
pygame.display.set_icon(icon)
intro=pygame.image.load('intro.png')
screen.blit(intro,(-5,0))
pygame.display.update()
pygame.time.wait(500)

intro_music= pygame.mixer.Sound('intro.mp3')
background_music= pygame.mixer.Sound('loop.mp3')
smashed_sound= pygame.mixer.Sound('hit.mp3')
game_over_music= pygame.mixer.Sound('gameOver.mp3')
background_music.set_volume(0.2)


class audio:
        # Load music and sound effects
    
    def play_intro_start():
        # Play intro music
        intro_music.play()
        # Simulate intro video or screen duration
        # time.sleep(4)  # assuming intro is 4 seconds long
    
    def play_intro_stop():    
        intro_music.stop()

    def play_background_music():
        # Play background music in a loop
        background_music.play(loops=-1)

    def play_smashed_sound():
        # Play smashed sound effect
        smashed_sound.play()

    def play_game_over():
        # Stop background music and play game over music
        background_music.stop()
        game_over_music.play()


video_path = "intro.mkv"
video = VideoFileClip(video_path)
pygame.display.set_caption('Game Intro')
def blit_frame(t):
    img = video.get_frame(t)
    img_surface = pygame.surfarray.make_surface(img.swapaxes(0, 1))
    return img_surface

# Main loop for the intro video
def play_intro():
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks() / 1000.0
    intro_running = True

    while intro_running:
        current_time = pygame.time.get_ticks() / 1000.0 - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    intro_running = False

        if current_time >= video.duration:
            intro_running = False

        frame_surface = blit_frame(current_time)
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()

        clock.tick(video.fps)



def game():

    playerImg=pygame.image.load('p3.png')
    playerX=855
    playerY=965
    playerX_change=0
    playerY_change=0

    def player(x,y):
        screen.blit(playerImg,(x,y)) 

    alienImg=pygame.image.load('monster (1).png')
    a=random.randint(0,1756)
    alienX=a
    alienY=10
    alienX_change=0.6
    alienY_change=0

    def alien(x,y):
        screen.blit(alienImg,(x,y)) 

    bulletImg=pygame.image.load('bullet.png')
    bulletX=playerX
    bulletY=playerY
    bulletX_change=0
    bulletY_change=8
    bullet_state=False

    def bullet(x,y):
        # global bullet_state
        bullet_state=True
        screen.blit(bulletImg,(x+20,y-30))

        # for y1 in range(y,0):
        #     screen.blit(bulletImg,(x,y1))

    def isCollision(a,b,c,d):
        if a<=c<=a+64 and b<=d<=b+64:
            return True
        else:
            return False

    score=0
    background=pygame.image.load("background.jpg")

    running=True

    while running:
        screen.fill((30,40,50,6))
        screen.blit(background,(0,0))
        
        if pygame.time.get_ticks()==60000: 
            running=False
            
        a=alienX
        b=alienY

        if a<=0:
            alienX_change=0.6
            alienY_change=60
        elif a>=1756:
            alienX_change=-0.6
            alienY_change=60
        else:
            alienY_change=0
        
        alienX=alienX+alienX_change
        alienY=alienY+alienY_change
        alien(alienX,alienY)


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
                    bullet(playerX,playerY)
                    bulletY=playerY
                    bulletX=playerX
                    bullet_state=True
                    audio.play_smashed_sound()
                if event.key==pygame.K_ESCAPE:
                    running=False

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    print("key is released")
                    playerX_change=0
                    playerY_change=0
                # if event.key==K_ESCAPE: 

        if bulletY<=0:
            bulletY=playerY
            bullet_state=False
        if bullet_state is True:
            bullet(bulletX,bulletY)
            bulletY=bulletY-bulletY_change

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
        
        collision=isCollision(alienX,alienY,bulletX+35,bulletY+35)
        if collision is True:
            score+=1
            print(score)
            a=random.randint(0,1756)
            alienX=a
            alienY=0

        pygame.display.update()


audio.play_intro_start()
play_intro()
screen.blit(intro,(-5,0))
pygame.time.wait(18)
audio.play_intro_stop()
audio.play_background_music()
game()
audio.play_game_over()