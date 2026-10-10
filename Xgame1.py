# p1-p11


import pygame
from moviepy.editor import VideoFileClip
import random
import time

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1820,1100))

clock1= pygame.time.Clock() 

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
explosion=pygame.mixer.Sound('explosion.mp3')

class audio:
        
    
    def play_intro_start():
        intro_music.play()
    
    def play_intro_stop():    
        intro_music.stop()

    def play_background_music():
        background_music.play(loops=-1)

    def play_smashed_sound():
        smashed_sound.play()

    def play_game_over():
        background_music.stop()
        game_over_music.play()
        

    def stop_game_over():
        game_over_music.stop()

    def explosion():
        explosion.play()


video_path = "intro.mkv"
video = VideoFileClip(video_path)
pygame.display.set_caption('Game Intro')
def blit_frame(t):
    img = video.get_frame(t)
    img_surface = pygame.surfarray.make_surface(img.swapaxes(0, 1))
    return img_surface

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

    alienImg=[]
    # a=random.randint(0,1756)
    alienX=[]
    alienY=[]
    alienX_change=[]
    alienY_change=[]
    num_of_aliens=10
    images=[pygame.image.load('monster (1).png'),pygame.image.load('monster (2).png'),pygame.image.load('monster (3).png')]
    for i in range(num_of_aliens):  
        alienImg.append(random.choice(images))
        a=random.randint(0,1756)
        alienX.append(a)
        alienY.append(50)
        alienX_change.append(random.choice([-1,1]))
        alienY_change.append(0)

    def alien(i,x,y):
        screen.blit(alienImg[i],(x,y)) 

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
        
    font=pygame.font.Font("font.otf",32)
    textX=10
    textY=10
    score_enemy=0

    font1=pygame.font.Font("font.otf",128)

    def game_over(score_enemy1,x,y):
        game_over=font1.render("Game Over",True,(255,255,255))
        total_score=font.render("Total score :"+str(score_enemy1),True,(255,255,255))
        screen.blit(game_over,(x,y))
        screen.blit(total_score,(x+100,y+135))

    def show_score(x,y):
        score=font.render("Score : "+str(score_enemy),True,(255,255,255,100))
        screen.blit(score,(x,y))
    
    background=pygame.image.load("background.jpg")

    running=True
    a1=0
    b1=False
    while running:
        if pygame.time.get_ticks()==60000: 
            running=False
            
        screen.fill((30,40,50,6))
        screen.blit(background,(0,0))
        
        for i in range(num_of_aliens):
            if (playerX<=alienX[i]<=playerX+64 and playerY<=alienY[i]<=playerY+64) or pygame.time.get_ticks()>=75000:
                audio.play_game_over()
                game_over(score_enemy,486,398)
                # pygame.time.wait(3000)
                pygame.display.update()
                b1=True
                break

            a1=alienX[i]
            b1=alienY[i]
            if a1<=0:
                alienX_change[i]=1
                alienY_change[i]=65
            elif a1>=1756:
                alienX_change[i]=-1
                alienY_change[i]=65
            else:
                alienY_change[i]=0

            alienX[i]=alienX[i]+alienX_change[i]
            alienY[i]=alienY[i]+alienY_change[i]
            collision=isCollision(alienX[i],alienY[i],bulletX+32,bulletY+32)
            if collision is True:
                audio.explosion()
                score_enemy+=1
                print(score_enemy)
                a=random.randint(0,1756)
                alienX[i]=a
                alienY[i]=50
            alien(i,alienX[i],alienY[i])




        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    print("left key is pressed")
                    playerX_change=-1.5
                if event.key==pygame.K_RIGHT:
                    print("right key is pressed")
                    playerX_change=1.5
                if event.key==pygame.K_UP:
                    print("up key is pressed")
                    playerY_change=-1.5
                if event.key==pygame.K_DOWN:
                    print("down key is pressed")
                    playerY_change=1.5
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
                    audio.play_game_over()
                    game_over(score_enemy,486,398)
                    # pygame.time.wait(3000)
                    pygame.display.update()
                    b1=True
                    break

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

        if (playerX>=0 and playerX<=1720) and (playerY>=700 and playerY<=1000): # 700 player y
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
        

        if b1 is True:
            pygame.time.wait(5000)
            running=False
            audio.stop_game_over()
        
        show_score(textX,textY)
        pygame.display.update()


audio.play_intro_start()
play_intro()
screen.blit(intro,(-5,0))
pygame.time.wait(18)
audio.play_intro_stop()
audio.play_background_music()
game()
# audio.play_game_over()