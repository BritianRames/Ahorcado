
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

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    window.blit(label1,(winWidth/2 - length/2, 400))
    pygame.draw.rect(window,(0, 153, 51),(winWidth/2-100,winHeight/2-100,230,250))
    pic = hangmanPics[limbs]
    window.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()

def randomWord():
    file = open("sentences.txt")
    f = file.readlines()
    i = random.randrange(0,len(f)-1)
    return f[i][:-1]

def buttonHit(x , y):
    for i in range(len(buttons)):
        if x < buttons[i][1]+20 and x > buttons[i][1]-20:
            if y < buttons[i][2]+20 and y > buttons[i][2]-20:
                if buttons[i][4] == True:
                    return buttons[i][5]
    return None

def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord


def end(winner = False):
    global limbs
    lostText = "GAME OVER!!!!"
    winText = "YOU WIN!!!!"
    replayText = "Press any key to play again..."
    redraw_game_window()
    pygame.time.delay(500)
    
    window.fill(GREEN)

    if winner == True:
        label = lost_font.render(winText, 1, BLACK)
    elif winner == False:
        label = lost_font.render(lostText, 1, BLACK)
    labelReplay = lost_font.render(replayText, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)
    window.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    window.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    window.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    window.blit(labelReplay, (winWidth / 2 - labelReplay.get_width() / 2, 190))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()

def reset():
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()
    print(word)

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
print(word)
inPlay = True
while inPlay:
    redraw_game_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
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