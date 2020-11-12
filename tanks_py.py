# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
#                                     Rudolf-Diesel-Fachschule                                  # 
#                                        script programming                                     #   
#                                               wit-a                                           #
#                                             tank Game                                         #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import the pygame library
import pygame, sys, time, random
from pygame.locals import *

# multipler
MULTIPLER = 20

# game fields
FIELDS = 30

# frames per second update game window
FPS = 60

# create a game field
game_window = pygame.display.set_mode((FIELDS * MULTIPLER, FIELDS * MULTIPLER))

# head title of game window
pygame.display.set_caption("Tanks")
game_active = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# colors in game
GRAY  = ( 138, 138, 138)
BLACK = ( 0, 0, 0)
WITHE  = ( 255, 255, 255)
BRICK_COLOR = (143, 38, 0)

# game icons 



# game map level 1
game_map=[
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0,],

[0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0,],
[0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0,],

[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],

[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],

[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],

[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
[0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0,],
]

# background game window
game_window.fill(GRAY)

# Korrekturfaktor berechnen
def correction_factor(correction_number):
    correction_number = correction_number * MULTIPLER
    return correction_number

# draw a game element
def draw_game_element(column,row):
    pygame.draw.rect(game_window, BRICK_COLOR, [correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1])

# print bricks in dame
for column in range(0,FIELDS):
    for row in range(0,FIELDS):
        if game_map[row][column] != 0:
            draw_game_element(column,row)

# main game loop
while game_active:
    # Check whether the user has taken an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_active = False
            print("GAME END BY USER")

    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

pygame.quit()