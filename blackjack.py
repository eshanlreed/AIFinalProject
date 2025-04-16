import copy
import random
import pygame

#game variables 
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4
game_deck = copy.deepcopy(decks * one_deck)
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Pygame Blackjack")
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
active = False

def draw_game():


#main game loop
run = True
while run:
    #run game at 60 fps and set background
    timer.tick(fps)
    screen.fill('black')
    buttons = draw_game(active)

    #event handling - quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit
