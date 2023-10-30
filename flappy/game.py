#!/usr/bin/python3
import subprocess
import random

# If have not pygame intalled installing
try:
    import pygame
except ImportError:
    print("pygame library not found. Installing...")
    subprocess.check_call(["pip", "install", "pygame"])
    import pygame

# Instalize pygame
pygame.init()

clock=pygame.time.Clock()

# Positions
bg_x=0
bird_x=200
bird_y=220
pipe_x=480
height_x=608
width_y=457
pipe_up_y2=0
pipe_up_y3=0
pipe_down_y2=0
pipe_down_y3=0  
pipe_down_y=random.choice(range(260, 370,10))
pipe_x2=0
pipe_x3=0
check=False
check_1=False
lose=True
score=0

# Import photos and Fonts
try:
    font=pygame.font.Font('font/Roboto-Black.ttf',26)
except pygame.error as e:
    print("Error loading font:", e)

try:
    font_big=pygame.font.Font('font/Roboto-Black.ttf',80)
except pygame.error as e:
    print("Error loading font:", e)

try:
    bg=pygame.image.load('images/bg.png')
except pygame.error as e:
    print("Error loading image:", e)

try:
    bird_up=pygame.image.load('images/bird_up.png')
except pygame.error as e:
    print("Error loading font:", e)

try:
    bird_down=pygame.image.load('images/bird_down.png')
except pygame.error as e:
    print("Error loading font:", e)

try:
    bird=pygame.image.load('images/bird.png')
except pygame.error as e:
    print("Error loading font:", e)
    
try:
    pipe_up=pygame.image.load('images/pipe_up.png') 
except pygame.error as e:
    print("Error loading font:", e)

try:
    pipe_down=pygame.image.load('images/pipe_down.png')
except pygame.error as e:
    print("Error loading font:", e)

try:
    replay=pygame.image.load('images/replay.png')
except pygame.error as e:
    print("Error loading font:", e)



replay=pygame.transform.scale(replay,(64,64))
pipe_up=pygame.transform.scale(pipe_up,(115,300))
pipe_down=pygame.transform.scale(pipe_down,(115,300))
bird_lose=pygame.transform.rotate(bird_down,-90)


# Create a screen
screen=pygame.display.set_mode((height_x , width_y))
pygame.display.set_caption("Flappy Bird")


# Game loop
run=True
while run:
    screen.blit(bg,(bg_x,0))    
    screen.blit(bg,(bg_x + 608,0))
       
    pipe_up_y=pipe_down_y-450
    
    screen.blit(pipe_up,(pipe_x,pipe_up_y))
    screen.blit(pipe_down,(pipe_x,pipe_down_y))
    
    
    # Pipe loops
    if pipe_x==(height_x//4):
        pipe_down_y2=random.choice(range(260, 370,30))
        pipe_up_y2=pipe_down_y2-450
        pipe_x2=680 
        check=True  
    if check:
        screen.blit(pipe_up,(pipe_x2,pipe_up_y2))    
        screen.blit(pipe_down,(pipe_x2,pipe_down_y2))
    if pipe_x2<-100:
        check=False

    if pipe_x2==(height_x//4):
        pipe_down_y3=random.choice(range(260, 370,20))
        pipe_up_y3=pipe_down_y3-450
        pipe_x3=680  
        check_1=True  
    if check_1:
        screen.blit(pipe_up,(pipe_x3,pipe_up_y3))    
        screen.blit(pipe_down,(pipe_x3,pipe_down_y3))
    if pipe_x3<-100:
        check_1=False
    if pipe_x<-100:
        pipe_x=680
    
    
    if abs(bg_x)>height_x:
        bg_x=0
    
    
    
    if bird_y>=376:
            lose=False
    
    # Keyprees
    key=pygame.key.get_pressed()
    if lose:
        if key[pygame.K_UP] or key[pygame.K_SPACE]:
            bg_x-=4
            pipe_x-=4
            pipe_x2-=4
            pipe_x3-=4
            bird_y-=4
            screen.blit(bird_up,(bird_x,bird_y))
        else:
            bg_x-=4
            pipe_x-=4
            pipe_x2-=4
            pipe_x3-=4
            bird_y+=4
            screen.blit(bird_down,(bird_x,bird_y))
        if bird_x>pipe_x or bird_x>pipe_x2 or bird_x>pipe_x3:
            if pipe_x==100 or pipe_x2==100 or pipe_x3==100:
                score+=1
        
    else:
        # Lose/Replay
        if bird_y<375:
            bird_y+=5
        screen.blit(bird_lose,(bird_x,bird_y))
        screen.blit(font_big.render("Lose!", True, "White"),(215,100))
        screen.blit(replay,(270,190))
        replay_rect=replay.get_rect(topleft=(270,190))
        mouse=pygame.mouse.get_pos()
        if replay_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lose=True
            bird_y=220
            score=0
            bg_x=0
            pipe_x=680
            pipe_x2=2000
            pipe_x3=2000
    
    # Rects
    bird_rect=bird_up.get_rect(topleft=(bird_x,bird_y))
    pipe_down_rect=pipe_down.get_rect(topleft=(pipe_x,pipe_down_y))
    pipe_up_rect=pipe_up.get_rect(topleft=(pipe_x,pipe_up_y))
    pipe_up_rect2=pipe_up.get_rect(topleft=(pipe_x2,pipe_up_y2))
    pipe_down_rect2=pipe_down.get_rect(topleft=(pipe_x2,pipe_down_y2))
    pipe_up_rect3=pipe_up.get_rect(topleft=(pipe_x3,pipe_up_y3))
    pipe_down_rect3=pipe_down.get_rect(topleft=(pipe_x3,pipe_down_y3))


    # Touch Bird to Pipes
    list_of_pipes=[pipe_down_rect,pipe_up_rect,pipe_down_rect2,pipe_up_rect2,pipe_down_rect3,pipe_up_rect3]
    if bird_rect.collidelistall(list_of_pipes):
        lose=False
    
    # Score
    score_text=font.render("Score: " + str(score), True, "White")
    screen.blit(score_text,(20,20)) 
    pygame.display.update()

    clock.tick(60)
    # Close page
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()