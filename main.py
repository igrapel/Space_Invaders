import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

#Get screen
screen = pygame.display.set_mode((700, 600))
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("SPACE INVADERS!!!!!")

#Load player object
playerImg = pygame.image.load("player.png")
playerX = 360
playerY = 540


def player(x, y):
    print("Player")
    screen.blit(playerImg, (x, y))


running = True
while running:

    #fill screen with a tuple of RBG Color
    screen.fill((10, 10, 200))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    #place player on screen
    player(playerX, playerY)
    pygame.display.update()