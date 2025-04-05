import pygame

from simulation import Simulation
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 10
FPS = 600
GREY = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sand simulation')

clock = pygame.time.Clock()
Simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

while True:

    Simulation.handle_controls()

    Simulation.update()

    window.fill(GREY)
    Simulation.draw(window)

    pygame.display.flip()
    clock.tick(FPS)