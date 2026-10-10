import pygame
from moviepy.editor import VideoFileClip
import random
import time

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((720,720))
clock=pygame.time.Clock()


pygame.display.set_caption("Snake Xenzia")
icon=pygame.image.load('logo2.png')
pygame.display.set_icon(icon)
intro=pygame.image.load('logo.png')
screen.blit(intro,(0,0))
pygame.display.update()
pygame.time.wait(300)


intro_music= pygame.mixer.Sound('')
background_music= pygame.mixer.Sound('')
smashed_sound= pygame.mixer.Sound('')
game_over_music= pygame.mixer.Sound('')
background_music.set_volume(0.2)
explosion=pygame.mixer.Sound('')


