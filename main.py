from typing import List

import pygame
from pygame import Color

from newClasses.Cube import Cube
from newClasses.Object import Object
from utils.types import Position, Rotation

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

environment: List[Object] = []
cube1: Cube = Cube(environment, screen, Position(0, 0, 2), Rotation(0, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    cube1.setPosition(cube1.pos + Position(0, 0, 0.01))

    pygame.draw.circle(screen, Color(255, 255, 255), (screen.get_width() / 2, screen.get_height() / 2), 5)

    for obj in environment:
        obj.tick()

    pygame.display.flip()

    clock.tick(60)
    # clock.tick()
    # print(clock.get_fps())

pygame.quit()
