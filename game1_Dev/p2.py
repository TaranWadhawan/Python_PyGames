# change title ,icon,background color etc
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

pygame.time.wait(2000)




# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
# game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        screen.fill((30,40,50,6))
        pygame.display.update()
# game code here