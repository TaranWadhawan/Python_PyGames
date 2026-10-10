# add intro video and audio

import pygame
from moviepy.editor import VideoFileClip

def play_intro(video_path):
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set the resolution as per your video

    # Load the video using moviepy
    clip = VideoFileClip(video_path)
    clip = clip.resize(height=600)  # Resize the video to fit the screen

    # Play the video
    for frame in clip.iter_frames(fps=30, dtype="uint8"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(surface, (0, 0))
        pygame.display.update()
        pygame.time.Clock().tick(30)

    clip.close()

def main_game():
    # Main game loop
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play_intro("intro.mkv")
    main_game()


# using ffpyplayer===pip install ffpyplayer
# import pygame
# from ffpyplayer.player import MediaPlayer

# def play_video(video_path):
#     def get_frame(player):
#         frame, val = player.get_frame()
#         if val == 'eof':
#             return None, None
#         return frame, val

#     # Initialize Pygame
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))  # Set the resolution as per your video
#     clock = pygame.time.Clock()

#     # Load the video using ffpyplayer
#     player = MediaPlayer(video_path)

#     playing = True
#     while playing:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 playing = False

#         frame, val = get_frame(player)
#         if frame is not None:
#             image, t = frame
#             # Convert the frame to a Pygame surface
#             frame_surface = pygame.image.frombuffer(image.to_bytearray()[0], image.get_size(), 'RGB')
#             screen.blit(frame_surface, (0, 0))
#             pygame.display.flip()

#         clock.tick(30)  # Ensure the video plays at 30 FPS

#     player.close()
#     pygame.quit()

# def main_game():
#     # Main game loop
#     screen = pygame.display.set_mode((800, 600))
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         screen.fill((0, 0, 0))  # Fill the screen with black
#         pygame.display.update()

#     pygame.quit()

# if __name__ == "__main__":
#     play_video("path_to_your_video.mp4")
#     main_game()

