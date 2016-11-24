import pygame
import time
import numpy as np
import random

pygame.init()
pygame.display.set_caption('Roonkie')

pygame.mixer.music.load("Track3.mp3")
pygame.mixer.music.play(-1)

def message_to_screen(msg, color, pos, font):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, pos)


# COLORS, RGB intensities
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
deep_blue = (0,191,255)
earth = (96,79,49)
meadow = (0,92,9)
skin = (255, 227, 159)
silver = (192,192,192)
red = (255,0,0)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

block_size = display_height/20

FPS = 30

g = 0.68

apple = pygame.image.load("apple.png")
newton = pygame.image.load("isaac_newton_bust_1.png")
mouth =  pygame.image.load("isaac_newton_bust_mouth_1.png")
tree = pygame.image.load("tree.png")
sky = pygame.image.load("sky.png").convert()

newtonrect = newton.get_rect()
newton_width, newton_height =  newtonrect.size

newton = pygame.transform.scale(newton, (newton_width/4,newton_height/4))
mouth  = pygame.transform.scale(mouth,  (newton_width/4,newton_height/4))
apple = pygame.transform.scale(apple, (40,40))
tree = pygame.transform.scale(tree, (display_width+200, 200))

lead_x = (display_width-block_size)/2
lead_y = display_height-block_size

lead_x_change = 0
lead_y_change = 0

apple_x = random.randrange(display_width - 40)
apple_y =  40
apple_speed = 0.0

clock = pygame.time.Clock()

top_font = pygame.font.SysFont("impact", display_height/25)
bot_font = pygame.font.SysFont("impact", 16)

img_time = 0

score = 0
eaten = 0
dropped = 0

gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                lead_x_change = -display_width/45
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                lead_x_change = display_width/45

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                lead_x_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                time.sleep(5)

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.blit(sky,(0,0))
    gameDisplay.blit(newton, (lead_x, lead_y-newton_height/4 + 10))
    pygame.draw.rect(gameDisplay, earth, [ 0, display_height-20, display_width, 20])
    gameDisplay.blit(apple , (apple_x, apple_y))
    gameDisplay.blit(tree , (-100,-100))
    
    if apple_y >= lead_y-148 and apple_y <= lead_y-108 and apple_x >= lead_x+68 and apple_x <= lead_x+148:
        img_time = 4
        apple_x = random.randrange(display_width - block_size)
        apple_y =  block_size
        apple_speed = 0
        score += 1
        eaten += 1
            
    else:
        apple_speed += g
        apple_y += int(apple_speed)

        
    if img_time > 0:
        gameDisplay.blit(mouth, (lead_x, lead_y-newton_height/4 + 10))
        img_time -= 1

    if apple_y > display_height - 40:
        apple_x = random.randrange(display_width - block_size)
        apple_y =  block_size
        apple_speed = 0
        score = 0
        dropped += 1

    message_to_screen("Eaten: "+ str(eaten), white, [5,0], top_font)
    message_to_screen("Score: "+ str(score), white, [display_width/2 - 35,0], top_font)
    message_to_screen("Dropped: "+ str(dropped), white, [display_width - 115,0], top_font)
    message_to_screen("Move left: left arrow key or a key" , white, [3,display_height-20], bot_font)
    message_to_screen("Exit: q or ESC" , white, [display_width/2-35 ,display_height-20], bot_font)
    message_to_screen("Move right: right arrow key or d key" , white, [display_width-230,display_height-20], bot_font)

    pygame.display.update()
    clock.tick(FPS)
    
message_to_screen("Game over", white, [display_width/2 - 20,display_height/2], top_font)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()


