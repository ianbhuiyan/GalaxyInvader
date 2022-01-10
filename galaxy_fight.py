
import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')
menubackground = pygame.image.load('y89nx9pal20z (1).png')

# Sound
mixer.music.load("The Music McCreamy uses In His Videos.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
#Change color of spaceship
playerImg2 = pygame.image.load('ufo.png')
playerX2 = 270
playerY2 = 480
playerX2_change = 0
playerY2_change = 0

menuspaceshipimg = pygame.image.load('realshiplesssssgo.png')
menuspaceshipX = 200
menuspaceshipY = 100
playbuttonimg = pygame.image.load('play_button.png')
playbuttonX = 60
playbuttonY = 400

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 9

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
enemyX[0]
enemyY[0]

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

bulletImg2 = pygame.image.load('bullet.png')
bulletX2 = 270
bulletY2 = 480
bulletX2_change = 0
bulletY2_change = 10
bullet_state2 = "ready"

enemybulletImg = pygame.image.load('bullet.png')
enemybulletX = enemyX[0]
enemybulletY = enemyY[0]
enemybulletX_change = 0
enemybulletY_change = -5
enemybullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 50)
font3 = pygame.font.Font('freesansbold.ttf', 47)


textX = 10
textY = 10

HP_value = 1

HPX = 655
HPY = 10

HP2_value = 1

HPX2 = 578
HPY2 = 40

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
multiplayerbutton = pygame.font.Font('freesansbold.ttf', 64)
helpbin = pygame.font.Font('freesansbold.ttf', 50)
gamecaption = pygame.font.Font('freesansbold.ttf', 85)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (64, 224, 208))
    screen.blit(score, (x, y))

def multiplayer():
    mul = font2.render("Multiplayer", True, (64, 224, 208))
    screen.blit(mul, (485, 470))

def gamelogo():
    gamelog = font3.render("SPACE INVADERS! LESS GO!", True, (64, 224, 208))
    screen.blit(gamelog, (90, 10))

def show_HP(x, y):
    score = font.render("Lives : " + str(HP_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

def show_HP2(x, y):
    score = font.render("UFO Lives : " + str(HP2_value), True, (78, 137, 117))
    screen.blit(score, (x, y))

def help():
    helpie = font.render("the Ufo controls are WASD", True, (64, 224, 208))
    screen.blit(helpie, (150, 60))
def game_over_text():
    over_text = over_font.render("GGS TRASH BIN", True, (0, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def player2(x, y):
    screen.blit(playerImg2, (x, y))

def playbutton(x, y):
    screen.blit(playbuttonimg, (x, y))

def menuspaceship(x, y):
    screen.blit(menuspaceshipimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def fire_bullet2(x, y):
    global bullet_state2
    bullet_state2 = "fire"
    screen.blit(bulletImg2, (x + 16, y + 10))

def fireenemy_bullet(x, y):
    global enemybullet_state
    enemybullet_state = "fire"
    screen.blit(enemybulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def isCollisionPlayer2(enemyX, enemyY, bulletX2, bulletY2):
    distance = math.sqrt(math.pow(enemyX - bulletX2, 2) + (math.pow(enemyY - bulletY2, 2)))
    if distance < 27:
        return True
    else:
        return False

def isPlayerCollision(playerX, playerY,enemybulletX, enemybulletY):
    enemydistance = math.sqrt(math.pow(playerX - enemybulletX, 2) + (math.pow(playerY - enemybulletY, 2)))
    if enemydistance < 27:
        return True
    else:
        return False

def isPlayer2Collision(playerX2, playerY2, enemybulletX, enemybulletY):
    enemydistance = math.sqrt(math.pow(playerX2 - enemybulletX, 2) + (math.pow(playerY2 - enemybulletY, 2)))
    if enemydistance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    screen.blit(menubackground, (0, 0))
    menuspaceship(menuspaceshipX, menuspaceshipY)
    playbutton(playbuttonX, playbuttonY)
    help()
    multiplayer()
    gamelogo()

    cursorX = pygame.mouse.get_pos()[0]
    cursorY = pygame.mouse.get_pos()[1]
    print(cursorX, cursorY)
    for event in pygame.event.get():
        if 80 < cursorX and cursorX < 239 and 446 < cursorY and cursorY < 520:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]:
                playerY2 = 10000
                HPY2 = -10000
                running = False
        if 486 < cursorX and cursorX < 761 and 464 < cursorY and cursorY < 504:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]:
                running = False
    '''
    for event in pygame.event.get():
        if 486 < cursorX and cursorX < 761 and 464 < cursorY and cursorY < 504:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]:
                running = False
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerX2_change = -5
                if event.key == pygame.K_d:
                    playerX2_change = 5
                if event.key == pygame.K_w:
                    playerY2_change = -5
                if event.key == pygame.K_s:
                    playerY2_change = 5
                if event.key == pygame.K_c:
                    if bullet_state2 == "ready":
                        bulletSound = mixer.Sound("Bruh Sound Effect #2.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX2 = playerX2
                        bulletY2 = playerY2
                        fire_bullet2(bulletX2, bulletY2)


        if enemybullet_state == "ready":
            bulletSound = mixer.Sound("Bruh Sound Effect #2.wav")
            bulletSound.play()
            # Get the current x cordinate of the spaceship
            enemybulletX = enemyX[0]
            enemybulletY = enemyY[0]
            fireenemy_bullet(enemybulletX, enemybulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX2_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY2_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 600:
        playerX = 600
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 600:
        playerY = 600

    playerX2 += playerX2_change
    if playerX2 <= 0:
        playerX2 = 0
    elif playerX2 >= 600:
        playerX2 = 600
    playerY2 += playerY2_change
    if playerY2 <= 0:
        playerY2 = 0
    elif playerY2 >= 600:
        playerY2 = 600

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 5
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        collisionPlayer2 = isCollisionPlayer2(enemyX[i], enemyY[i], bulletX2, bulletY2)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY2 = 480
            bullet_state2 = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
        Playercollision = isPlayerCollision(playerX, playerY, enemybulletX, enemybulletY)
        if Playercollision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            enemybulletY = 2000
            enemybullet_state = "ready"
            HP_value -= 1
            if HP_value == 0:
                playerX = 50000
                playerY = 10000
                HPY = 10000
                HPY2 = 10

        enemy(enemyX[i], enemyY[i], i)
        Player2collision = isPlayer2Collision(playerX2, playerY2, enemybulletX, enemybulletY)
        if Player2collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            enemybulletY = 2000
            enemybullet_state = "ready"
            HP2_value -= 1
            if HP2_value == 0:
                playerY2 = 10000
                playerX2 = 50000
                HPY2 = 10000

    if HP_value == 0 and HP2_value == 0:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        game_over_text()



    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY2 <= 0:
        bulletY2 = 480
        bullet_state2 = "ready"

    if bullet_state2 == "fire":
        fire_bullet2(bulletX2, bulletY2)
        bulletY2 -= bulletY2_change

    if enemybulletY >= 600:
        enemybulletY = enemyY[0]
        enemybulletX = enemyX[0]
        enemybullet_state = "ready"

    if enemybulletX >= 800:
        enemybulletY = enemyY[0]
        enemybulletX = enemyX[0]
        enemybullet_state = "ready"

    if enemybullet_state == "fire":
        enemybulletY -= enemybulletY_change
        enemybulletX += enemybulletX_change
        fireenemy_bullet(enemybulletX, enemybulletY)

    player(playerX, playerY)
    player2(playerX2, playerY2)
    show_score(textX, textY)
    show_HP(HPX, HPY)
    show_HP2(HPX2, HPY2)
    pygame.display.update()
