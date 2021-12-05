import pygame
import random

pygame.init()

screen = pygame.display.set_mode([1024,768])

# Load Sound effects
squeakSound = pygame.mixer.Sound("audio/guinea_squeak.mp3")
squeakSound.set_volume(0.5)

startSound = pygame.mixer.Sound("audio/start_sound.wav")

# Load graphics
grassImg = pygame.image.load("images/grass1.png")
grassImg = pygame.transform.scale(grassImg, (128,128))

berrybushImg = pygame.image.load("images/berrybush1.png")
berrybushImg = pygame.transform.scale(berrybushImg, (128,99))

brownieImg = pygame.image.load("images/player1.png")

player1 = pygame.image.load("images/player1.png")
player1 = pygame.transform.scale(player1, (80,62))

player1_talk = pygame.image.load("images/player1_squeak.png")
player1_talk = pygame.transform.scale(player1_talk, (80,62))

player1Rect = player1.get_rect()
player1Rect.center = (480,700)

player1_talkRect = player1_talk.get_rect()
player1_talkRect.center = (480,700)

startBtn = pygame.image.load("images/button_start.png")

fontFill = (53, 49, 48)
menuFont = pygame.font.Font("PressStart2P-Regular.ttf", 48)
menuText = menuFont.render("Brownie's Adventure", True, fontFill)
menuRect = menuText.get_rect()
menuRect.center = (500, 130)

print("Running")

running = True
gameloop = False

p1_x = 340
p1_y = 900


def playSound(sound):
    pygame.mixer.Sound.play(sound)
    

while running:

    screen.fill((175,235,160))
    start_click = screen.blit(startBtn, (220, 580))
    screen.blit(brownieImg, (370,250))
    screen.blit(menuText, menuRect)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if event.button == 1:
                print(pos)
                if start_click.collidepoint(pos):
                    print("Start Button Clicked")
                    playSound(startSound)
                    running=False
                    gameloop=True
                else:
                    print("Clicked elsewhere")
    
    pygame.display.flip()

x=0
y=0
talking = False

current_time = pygame.time.get_ticks()
next_move = current_time + 200

# Load and start playing background music
pygame.mixer.music.load("audio/bg_music1.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(0)

# Allow key-repeating
pygame.key.set_repeat(1, 60)

while gameloop:

    screen.fill((175,235,160))

    #Draw grass
    grass_x=0
    grass_y=0
    while grass_y < 700:
        screen.blit(grassImg, (grass_x,grass_y))
        grass_x+=128
        if grass_x > 900:
            grass_x=0
            grass_y+=128

    # Draw berries
    screen.blit(berrybushImg, (256,512))
    screen.blit(berrybushImg, (0,512))
    screen.blit(berrybushImg, (512,128))
    screen.blit(berrybushImg, (720,256))
    screen.blit(berrybushImg, (128,128))





    # Switch Guinea's face when he speaks
    current_time = pygame.time.get_ticks()
    if next_move <= current_time and talking is True:
        talking = False

    if talking:
        screen.blit(player1_talk,player1Rect)
    else:
        screen.blit(player1,player1Rect)

    player1Rect = player1Rect.move((x,y))
    x=0
    y=0

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y=-24
            elif event.key == pygame.K_DOWN:
                y=24
            elif event.key == pygame.K_LEFT:
                x=-24
            elif event.key == pygame.K_RIGHT:
                x=24
            elif event.key == pygame.K_SPACE and talking==False:
                playSound(squeakSound)
                screen.blit(player1_talk,player1Rect)
                next_move = current_time + 200
                talking = True


    pygame.display.flip()


pygame.quit()