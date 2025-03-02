import pygame
from player import Player
from constants import *


def main():
    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen: pygame.display  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0
    player: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        player.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60) / 1000


if __name__ == "__main__":
    main()
