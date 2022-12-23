import pygame
from fighter import Fighter

pygame.init()

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #command for display
pygame.display.set_caption("Brawler")

#set framerate
clock=pygame.time.Clock()
FPS=60

#define colors
RED = (255,0,0) 
YELLOW = (255,255,0)
WHITE = (255,255,255)

#define fighter variables
HERO_SIZE=200
HERO_SCALE=4
HERO_OFFSET=[90,75]
HERO_DATA=[HERO_SIZE,HERO_SCALE,HERO_OFFSET]
WIZARD_SIZE=200
WIZARD_SCALE=2.8
WIZARD_OFFSET=[75,75]
WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]


#background image
bg_image=pygame.image.load("assets/images/background/background.gif").convert_alpha()#load to memory

#load spritesheets
hero_sheet=pygame.image.load("assets/images/Hero/Sprites/Hero.png").convert_alpha()
wizard_sheet=pygame.image.load("assets/images/Wizard/Sprites/Wizard.png").convert_alpha()

#define number of steps in each animation
HERO_ANIMATION_STEPS=[8,8,2,6,6,4,6]
WIZARD_ANIMATION_STEPS=[6,8,2,8,8,4,7]

#function for drawing image
def draw_bg():
    scaled_bg=pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#function for drawing fighter health bars
def draw_health_bar(health,x,y):
    ratio=health/100
    pygame.draw.rect(screen,WHITE,(x-2,y-2,404,34))
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen,YELLOW,(x,y,400*ratio,30))

#create two instances of fighters
fighter_1 = Fighter(200,450,False,HERO_DATA,hero_sheet,WIZARD_ANIMATION_STEPS)
fighter_2 = Fighter(700,450,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS)


#game loop
run = True
while run:

    clock.tick(FPS)
    #draw nack ground
    draw_bg()
    
    #show player stats
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,860,20)

    #move fighters
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    #update display
    pygame.display.update()

#exit pygame
pygame.quit()



