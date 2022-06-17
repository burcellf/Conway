import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

# window size
width, height = 1650, 1050
size = (width, height)

pygame.init()
pygame.display.set_caption('game of life')
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

# some colors
black = (0, 0, 0)
charcoal = (22, 22, 22)
dark_gray = (30, 30, 30)
dark_blue = (10, 61, 110)
med_blue = (0, 121, 150)
cherry = (200, 14, 71)

# size of each cell and its boarder
scaler, offset = 15, 5

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(dark_gray)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    Grid.Conway(off_color=charcoal, on_color=dark_blue, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    pygame.display.update()

pygame.quit()
