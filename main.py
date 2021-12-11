'''
MarioBros clone
Written by Canahedo
Python3
2021
'''

import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Set window size, create window, and set title bar
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MarioBros Clone")

# Color variables for readability
WHITE = (255, 255, 255)

# Game variables
FPS = 60

# Set player sprites and background image
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', '1280px-SSBU-Mario_Bros.png')), (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(BACKGROUND, (0,0)) # Background image
    pygame.display.update() # Refresh screen

def main():
    clock = pygame.time.Clock()
    run = True
    while run: # set run false to end game loop
        clock.tick(FPS) # Set game clock to FPS variable
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Closed window event
                run = False
                pygame.quit()
        
        draw_window()

# Cuz you're supposed to, I guess
if __name__ == "__main__":
    main()