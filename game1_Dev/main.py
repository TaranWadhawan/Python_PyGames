import pygame

#initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((500,500))
clock=pygame.time.clock()
screen.fill((255,255,255))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)