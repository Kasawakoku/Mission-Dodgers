# Bruce Qiu
# Simple Game
# Partner: Jonathan Fong
import pygame
import random
import math
import time
from pygame.locals import K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 480
HEIGHT = 320
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Global Variables

# Character
character_y = 160
character_x = 60

# Clouds
cloud1_x = 205
cloud1_y = 50
cloud2_x = 195
cloud2_y = 130
cloud3_x = 305
cloud3_y = 180
cloud4_x = 440
cloud4_y = 310
cloud5_x = 40
cloud5_y = 205

# Obstacles
obstacle1_x = 480
obstacle1_y = random.randrange(0,311)
obstacle1_speed = random.randrange(10,21) / 10

obstacle2_x = 480
obstacle2_y = random.randrange(0,311)
obstacle2_speed = random.randrange(10,21) / 10

obstacle3_x = 480
obstacle3_y = random.randrange(0,311)
obstacle3_speed = random.randrange(10,21) / 10

obstacle4_x = 480
obstacle4_y = random.randrange(0,311)
obstacle4_speed = random.randrange(10,21) / 10

# Healthbar
lives = 3
bar_height = 25
bar_max_width = 90
bar_x = 200
bar_y = HEIGHT//2

framecount = 0
print("Avoid the enemy!")
# Timer
start_time = time.time()

running = True
while running:
    # Events
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[K_UP] and not character_y == 25:
            character_y -= 5
        elif keys[K_DOWN] and not character_y == 295:
            character_y += 5
        elif keys[K_LEFT] and not character_x == 30:
            character_x -= 5
        elif keys[K_RIGHT] and not character_x == 450:
            character_x += 5
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        

    # Clouds
    cloud1_x -= 0.5
    if cloud1_x < -55:
        cloud1_x = 500
        
    cloud2_x += 0.75
    if cloud2_x > 535:
        cloud2_x = -20
        
    cloud3_x -= 0.3
    if cloud3_x < -55:
        cloud3_x = 500
        
    cloud4_x += 0.9
    if cloud4_x > 535:
        cloud4_x = -20
        
    cloud5_x -= 0.1
    if cloud5_x < -55:
        cloud5_x = 500

    # Obstacles
    obstacle1_x -= obstacle1_speed
    if obstacle1_x < -60:
        obstacle1_x = 480
        obstacle1_y = random.randrange(0,311)
        obstacle1_box = pygame.Rect(obstacle1_x,obstacle1_y,40,10)
        obstacle1_speed = random.randrange(10,21) / 10

    obstacle2_x -= obstacle2_speed
    if obstacle2_x < -60:
        obstacle2_x = 480
        obstacle2_y = random.randrange(0,311)
        obstacle2_box = pygame.Rect(obstacle2_x,obstacle2_y,40,10)
        obstacle2_speed = random.randrange(10,21) / 10

    obstacle3_x -= obstacle3_speed
    if obstacle3_x < -60:
        obstacle3_x = 480
        obstacle3_y = random.randrange(0,311)
        obstacle3_box = pygame.Rect(obstacle3_x,obstacle3_y,40,10)
        obstacle3_speed = random.randrange(10,21) / 10

    obstacle4_x -= obstacle1_speed
    if obstacle4_x < -60:
        obstacle4_x = 480
        obstacle4_y = random.randrange(0,311)
        obstacle4_box = pygame.Rect(obstacle4_x,obstacle4_y,40,10)
        obstacle4_speed = random.randrange(10,21) / 10

    # sin motion
    origin_x = WIDTH//2
    origin_y = HEIGHT//2
    radius = 200

    framecount += 1
    a = framecount / 60

    obstacle5_x = math.sin(a) * radius + origin_x 
    obstacle5_y = math.cos(a) * radius + origin_y
        
    # Background
    screen.fill((15,15,15))

    # Moon
    pygame.draw.circle(screen,(155,155,155),(420,35),30)
    pygame.draw.circle(screen,(15,15,15),(410,25),30)

    # Clouds
    pygame.draw.circle(screen,(35,35,35),(cloud1_x,cloud1_y),20)
    pygame.draw.circle(screen,(35,35,35),(cloud1_x-10,cloud1_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud1_x+15,cloud1_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud1_x+30,cloud1_y-2),20)
    pygame.draw.circle(screen,(35,35,35),(cloud1_x+45,cloud1_y+20),20)

    pygame.draw.circle(screen,(35,35,35),(cloud2_x,cloud2_y),20)
    pygame.draw.circle(screen,(35,35,35),(cloud2_x-10,cloud2_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud2_x+15,cloud2_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud2_x+30,cloud2_y-2),20)
    pygame.draw.circle(screen,(35,35,35),(cloud2_x+45,cloud2_y+20),20)

    pygame.draw.circle(screen,(35,35,35),(cloud3_x,cloud3_y),20)
    pygame.draw.circle(screen,(35,35,35),(cloud3_x-10,cloud3_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud3_x+15,cloud3_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud3_x+30,cloud3_y-2),20)
    pygame.draw.circle(screen,(35,35,35),(cloud3_x+45,cloud3_y+20),20)

    pygame.draw.circle(screen,(35,35,35),(cloud4_x,cloud4_y),20)
    pygame.draw.circle(screen,(35,35,35),(cloud4_x-10,cloud4_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud4_x+15,cloud4_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud4_x+30,cloud4_y-2),20)
    pygame.draw.circle(screen,(35,35,35),(cloud4_x+45,cloud4_y+20),20)

    pygame.draw.circle(screen,(35,35,35),(cloud5_x,cloud5_y),20)
    pygame.draw.circle(screen,(35,35,35),(cloud5_x-10,cloud5_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud5_x+15,cloud5_y+15),20)
    pygame.draw.circle(screen,(35,35,35),(cloud5_x+30,cloud5_y-2),20)
    pygame.draw.circle(screen,(35,35,35),(cloud5_x+45,cloud5_y+20),20)

    
    # Character
    pygame.draw.circle(screen,(232,163,23),(character_x-20,character_y),7)
    pygame.draw.polygon(screen,(0,78,56),((character_x,character_y),(character_x-18,character_y+25),(character_x-10,character_y),(character_x-18,character_y-25)))
    pygame.draw.polygon(screen,(11,102,35),((character_x,character_y),(character_x-30,character_y+15),(character_x-20,character_y),(character_x-30,character_y-15)))

    character_box = pygame.Rect(character_x-30,character_y-25,30,50)
    
    # Obstacles
    pygame.draw.polygon(screen,(188,0,0),((obstacle1_x+50,obstacle1_y+10),(obstacle1_x+58,obstacle1_y),(obstacle1_x+58,obstacle1_y+20)))
    pygame.draw.ellipse(screen,(144,0,0),(obstacle1_x,obstacle1_y,60,20))
    obstacle1_box = pygame.Rect(obstacle1_x,obstacle1_y,60,20)

    pygame.draw.polygon(screen,(188,0,0),((obstacle2_x+50,obstacle2_y+10),(obstacle2_x+58,obstacle2_y),(obstacle2_x+58,obstacle2_y+20)))
    pygame.draw.ellipse(screen,(144,0,0),(obstacle2_x,obstacle2_y,60,20))
    obstacle2_box = pygame.Rect(obstacle2_x,obstacle2_y,60,20)

    pygame.draw.polygon(screen,(188,0,0),((obstacle3_x+50,obstacle3_y+10),(obstacle3_x+58,obstacle3_y),(obstacle3_x+58,obstacle3_y+20)))
    pygame.draw.ellipse(screen,(144,0,0),(obstacle3_x,obstacle3_y,60,20))
    obstacle3_box = pygame.Rect(obstacle3_x,obstacle3_y,60,20)

    pygame.draw.polygon(screen,(188,0,0),((obstacle4_x+50,obstacle4_y+10),(obstacle4_x+58,obstacle4_y),(obstacle4_x+58,obstacle4_y+20)))
    pygame.draw.ellipse(screen,(144,0,0),(obstacle4_x,obstacle4_y,60,20))
    obstacle4_box = pygame.Rect(obstacle4_x,obstacle4_y,60,20)

    pygame.draw.rect(screen,(124,13,14),(obstacle5_x,obstacle5_y,30,30))
    pygame.draw.polygon(screen,(180,13,14),((obstacle5_x,obstacle5_y),(obstacle5_x+15,obstacle5_y-5),(obstacle5_x+30,obstacle5_y)))
    obstacle5_box = pygame.Rect(obstacle5_x,obstacle5_y-5,30,35)

    # Hitbox
    if character_box.colliderect(obstacle1_box) or character_box.colliderect(obstacle2_box) or character_box.colliderect(obstacle3_box) or character_box.colliderect(obstacle4_box) or character_box.colliderect(obstacle5_box):
        lives -= 1
        obstacle1_x = -61
        obstacle2_x = -61
        obstacle3_x = -61
        obstacle4_x = -61
        framecount = 0
        
        character_y = 160
        character_x = 60

    # Healthbars
    if lives > 0:
        pygame.draw.rect(screen, (0, 200, 0), (0, 0, lives*30, bar_height))
        pygame.draw.rect(screen, (200, 200, 200), (0, 0, bar_max_width, bar_height), 2)
    
    else:
        time_elapsed = time.time() - start_time 
        pygame.draw.rect(screen, (200, 200, 200), (0, 0, bar_max_width, bar_height),2)
        time.sleep(1)
        running = False
        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
print("Good game!")
print(f"You lasted {round(time_elapsed,2)} seconds!")