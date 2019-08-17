
import pygame
import random

pygame.init()

#########################################################
## Set Frame dimmension                                ##
#########################################################
winWidth = 1000
winHeight = 600
win = pygame.display.set_mode((winWidth,winHeight))

#########################################################
## Initialize global variables/constants               ##
#########################################################

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('./img/hangman0.png'), pygame.image.load('./img/hangman1.png'), pygame.image.load('./img/hangman2.png'), pygame.image.load('./img/hangman3.png'), pygame.image.load('./img/hangman4.png'), pygame.image.load('./img/hangman5.png'), pygame.image.load('./img/hangman6.png')]



pygame.quit()

# always quit pygame when done!