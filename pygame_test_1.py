# imports
import pygame
import os
pygame.init()

# variables
FPS = 60
WIDTH, HEIGHT = 900, 800
GAME_TITLE = "insert title here"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# window setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# load images
# create assets folder and use os.path.join('assets', 'your image name')
# make sure your image is a png!

# main function
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
