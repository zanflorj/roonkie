#################################################################
# Created by Zan Florjanc "zan.florjanc@gmail.com" on 24nov2016 #
#################################################################

import pygame
import time
import numpy as np
import random

#initialize
pygame.init()
pygame.display.set_caption('Roonkie')

#function that displays text of certain color, at ceratin position on screen, with specified font
def message_to_screen(msg, color, pos, font):
    screen_text = font.render(msg, True, color)
    GAME_DISPLAY.blit(screen_text, pos)


#    
#GLOBALS
#

#Colors
WHITE = (255,255,255)
EARTH = (96,79,49)

#Window
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#Block to use when moving and blitting surfaces
BLOCK = DISPLAY_HEIGHT//20

#Frames per second
FPS = 30

#Gravity
G = 0.68

#Images
APPLE = pygame.image.load("apple.png")
NEWTON = pygame.image.load("isaac_newton_bust_1.png")
MOUTH =  pygame.image.load("isaac_newton_bust_mouth_1.png")
TREE = pygame.image.load("tree.png")
SKY = pygame.image.load("sky.png").convert()

#Clock 
CLOCK = pygame.time.Clock()

#Fonts 
T_FONT = pygame.font.SysFont("impact", DISPLAY_HEIGHT//25)
B_FONT = pygame.font.SysFont("impact", 16)

#load music
pygame.mixer.music.load("Cinglbong.mp3")
pygame.mixer.music.play(-1)

def main():
    #
    #locals
    #

    gameExit = False

    #coordinates for newton
    lead_x = (DISPLAY_WIDTH-BLOCK)/2
    lead_y = DISPLAY_HEIGHT-BLOCK

    #Newton speed
    lead_x_change = 0
    lead_y_change = 0

    #Scoring system
    score = 0
    eaten = 0
    dropped = 0

    #Varible to determine when to blit MOUTH
    img_time = 0

    #Apple coors and speed
    apple_x = random.randrange(DISPLAY_WIDTH - 40)
    apple_y =  40
    apple_speed = 0.0

    #get rect for Newton and resize everythin so it fits
    newtonrect = NEWTON.get_rect()
    newton_width, newton_height =  newtonrect.size

    newton = pygame.transform.scale(NEWTON, (newton_width/4,newton_height/4))
    mouth  = pygame.transform.scale(MOUTH,  (newton_width/4,newton_height/4))
    apple = pygame.transform.scale(APPLE, (40,40))
    tree = pygame.transform.scale(TREE, (DISPLAY_WIDTH+200, 200))
    
    #game loop
    while not gameExit:

        #check user input
        
        for event in pygame.event.get():
            #key is down
            if event.type == pygame.KEYDOWN:
                #exit
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    gameExit = True

                #move left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    lead_x_change = -DISPLAY_WIDTH/45
                #move right
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    lead_x_change = DISPLAY_WIDTH/45

                #take a short break
                if event.key == pygame.K_p:
                    time.sleep(5)

            #key is up        
            if event.type == pygame.KEYUP:
                #stop moving
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    lead_x_change = 0
                           
        #assign new position
        lead_x += lead_x_change
        lead_y += lead_y_change

        #draw everything on surface
        GAME_DISPLAY.blit(SKY,(0,0))
        GAME_DISPLAY.blit(newton, (lead_x, lead_y-newton_height/4 + 10))
        GAME_DISPLAY.blit(apple , (apple_x, apple_y))
        GAME_DISPLAY.blit(tree , (-100,-100))
        pygame.draw.rect(GAME_DISPLAY, EARTH, [ 0, DISPLAY_HEIGHT-20, DISPLAY_WIDTH, 20])
       
        #check if apple can be eaten
        if apple_y >= lead_y-148 and apple_y <= lead_y-108 and apple_x >= lead_x+68 and apple_x <= lead_x+148:
            img_time = 4
            apple_x = random.randrange(DISPLAY_WIDTH-BLOCK)
            apple_y =  BLOCK
            apple_speed = 0
            score += 1
            eaten += 1

        #if it isn't, keeps falling    
        else:
            apple_speed += G
            apple_y += int(apple_speed)

        #open newtons mouth
        if img_time > 0:
            GAME_DISPLAY.blit(mouth, (lead_x, lead_y-newton_height/4 + 10))
            img_time -= 1

        #check if apple has fallen to the ground
        if apple_y > DISPLAY_HEIGHT - 40:
            apple_x = random.randrange(DISPLAY_WIDTH-BLOCK)
            apple_y =  BLOCK
            apple_speed = 0
            score = 0
            dropped += 1

        #print some info on screen for user
        message_to_screen("Eaten: "+ str(eaten), WHITE, [5,0], T_FONT)
        message_to_screen("Score: "+ str(score), WHITE, [DISPLAY_WIDTH/2 - 35,0], T_FONT)
        message_to_screen("Dropped: "+ str(dropped), WHITE, [DISPLAY_WIDTH - 125,0], T_FONT)
        message_to_screen("Move left: left arrow key or a key" , WHITE, [3,DISPLAY_HEIGHT-20], B_FONT)
        message_to_screen("Exit: q or ESC" , WHITE, [DISPLAY_WIDTH/2-35 , DISPLAY_HEIGHT-20], B_FONT)
        message_to_screen("Move right: right arrow key or d key" , WHITE, [DISPLAY_WIDTH-230, DISPLAY_HEIGHT-20], B_FONT)

        #update all
        pygame.display.update()
        CLOCK.tick(FPS)

    #when game loop closes
    message_to_screen("Game over", WHITE, [DISPLAY_WIDTH/2 - 20, DISPLAY_HEIGHT/2], T_FONT)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()


