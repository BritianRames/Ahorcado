
import pygame
import random

pygame.init()

#########################################################
## Set Frame dimmension                                ##
#########################################################
winWidth = 700
winHeight = 480
window = pygame.display.set_mode((winWidth,winHeight))

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

limbs = 0


def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    window.fill(GREEN)
    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(window, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(window, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            window.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    ##spaced = spacedOut(word, guessed)
    ##label1 = guess_font.render(spaced, 1, BLACK)
    ##rect = label1.get_rect()
    ##length = rect[2]
    
    ##window.blit(label1,(winWidth/2 - length/2, 400))
    pygame.draw.rect(window,(0, 153, 51),(winWidth/2-100,winHeight/2-100,230,250))
    pic = hangmanPics[limbs]
    window.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()

def randomWord():
    file = open("palabras.txt")
    f = file.readlines()
    i = random.randrange(0,len(f)-1)
    return f[i][:-1]

#########################################################
## Setup buttons.                                      ##
## Need to identify which letter is pressed            ##
#########################################################
increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
    # buttons.append([color, x_pos, y_pos, radius, visible, char])

word = randomWord()
inPlay = True

while inPlay:
    redraw_game_window()
    #pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            #letter = buttonHit(clickPos[0], clickPos[1])
            if letter != None:
                guessed.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    if limbs != 5:
                        limbs += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()

# always quit pygame when done!