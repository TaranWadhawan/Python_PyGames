# add music
import pygame
import time

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load music and sound effects
intro_music= pygame.mixer.Sound('intro.mp3')
background_music= pygame.mixer.Sound('loop.mp3')
smashed_sound= pygame.mixer.Sound('hit.mp3')
game_over_music= pygame.mixer.Sound('gameOver.mp3')
background_music.set_volume(0.2)
def play_intro():
    # Play intro music
    intro_music.play()
    # Simulate intro video or screen duration
    time.sleep(5)  # assuming intro is 5 seconds long
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

def main_game():
    # Main game loop
    screen = pygame.display.set_mode((800, 600))
    running = True
    play_background_music()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Simulate a smash action
                    play_smashed_sound()
                if event.key == pygame.K_q:  # Simulate game over
                    play_game_over()
                    time.sleep(3)  # assuming game over duration is 3 seconds
                    running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play_intro()
    main_game()
