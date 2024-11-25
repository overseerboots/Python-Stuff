import pygame
import random
import math

# Ship ------------------------------------------
ship_x = 300
ship_y = 700
direction = 0
speed = 8

# Bullet ----------------------------------------
bullet = False
bullet_x = 0
bullet_y = 0
bullet_speed = 12

# Enemy -----------------------------------------
enemies = []
wobble = 0
counter = 0 # Count the frames
counter_limit = 50 # 2 seconds

def make_new_enemy():
    # [X, Y, Speed]
    enemy = [random.randint(30,550), 50, 3]
    enemies.append(enemy)

def box_collision(e):
    if bullet_x >= e[0] and bullet_x <= e[0] + 93:
        if bullet_y >= e[1] and bullet_y <= e[1] + 84:
            return True
    return False

# Setup -----------------------------------------
fps = 60
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Game")
screen = pygame.display.set_mode((600,800))

# Load Images -----------------------------------
background = pygame.image.load("assets/stars.png").convert()
bigger_background = pygame.transform.scale(background, (600,800)).convert()
ship = pygame.image.load("assets/ship.png").convert_alpha()
bullet_img = pygame.image.load("assets/bullet.png").convert()
enemy_img = pygame.image.load("assets/enemy.png").convert_alpha()

# Game Loop =====================================
running = True
while running:
    # Process events ----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = -1
            if event.key == pygame.K_RIGHT:
                direction = 1
            if event.key == pygame.K_SPACE:
                if bullet == False:
                    bullet = True
                    bullet_x = ship_x + 48
                    bullet_y = ship_y - 24


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = 0 # Stop
            if event.key == pygame.K_RIGHT:
                direction = 0 # Stop

    # Update game logic -------------------------
    wobble = wobble + 4 # 4 Degrees at a time
    if wobble >= 360:
        wobble = 0
    
    counter = counter + 1
    if counter >= counter_limit:
        make_new_enemy()
        counter = 0

    ship_x += direction * speed # Player ship

    # Update enemies ----------------------------
    for enemy in enemies:
        #   y    =  y       +   speed
        enemy[1] = enemy[1] + enemy[2]
        enemy[0] = enemy[0] + (math.sin(math.radians(wobble)))

        if enemy[1] > 800:
            enemies.remove(enemy)
        
    # Check if bullet has hit any enemies
    if bullet:
        for enemy in enemies:
            if box_collision(enemy):
                bullet = False
                enemies.remove(enemy)

    # Bullet ------------------------------------
    if bullet == True:
        bullet_y = bullet_y - bullet_speed
        if bullet_y < 0:
            bullet = False


    # Draw screen -------------------------------
    screen.blit(bigger_background,(0,0))
    screen.blit(ship,(ship_x,ship_y))
    
    if bullet == True:
        screen.blit(bullet_img,(bullet_x,bullet_y))

    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0],enemy[1]))

    # Update the buffer -------------------------
    pygame.display.flip()
    clock.tick(fps)