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

# Background
background = pygame.image.load('background.png')

#Load player object
playerImg = pygame.image.load("player.png")
playerX = 360
playerY = 540

# Caption and Icon
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = 370
enemyY = 30
enemyX_change = 2
enemyY_change = 10



# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

running = True
while running:

    #fill screen with a tuple of RBG Color
    screen.fill((10, 10, 200))

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_s:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 670:
            playerX = 670

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyY = enemyY + enemyY_change
        enemyX_change = 2

    elif enemyX >= 670:
        enemyY = enemyY + enemyY_change
        enemyX_change = -2


    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

        # places player on the screen
    player(playerX, playerY)

    enemy(enemyX, enemyY)
    pygame.display.update()