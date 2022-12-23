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

#define game variables
intro_count=3
last_count_update=pygame.time.get_ticks()
score=[0,0]#player 1 and 2 score respectively
round_over=False
ROUND_OVER_COOLDOWN=2000

#define fighter variables
HERO_SIZE=200
HERO_SCALE=4
HERO_OFFSET=[90,75]
HERO_DATA=[HERO_SIZE,HERO_SCALE,HERO_OFFSET]
WIZARD_SIZE=190
WIZARD_SCALE=2.8
WIZARD_OFFSET=[75,75]
WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]


#background image
bg_image=pygame.image.load("assets/images/background/background.gif").convert_alpha()#load to memory

#load spritesheets
hero_sheet=pygame.image.load("assets/images/Hero/Sprites/Hero.png").convert_alpha()
wizard_sheet=pygame.image.load("assets/images/Wizard/Sprites/Wizard.png").convert_alpha()

#load victory
victory_img=pygame.image.load("assets/images/icons/victory.png").convert_alpha()

#define number of steps in each animation
HERO_ANIMATION_STEPS=[8,8,2,6,6,4,6]
WIZARD_ANIMATION_STEPS=[6,8,2,8,8,4,7]

#define font
count_font=pygame.font.Font("assets/fonts/turok.ttf",80)
score_font=pygame.font.Font("assets/fonts/turok.ttf",30)

#for drawing function
def draw_text(text,font,text_color,x,y):
    img=font.render(text,True,text_color)
    screen.blit(img,(x,y))

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
fighter_1 = Fighter(1,200,450,False,HERO_DATA,hero_sheet,WIZARD_ANIMATION_STEPS)
fighter_2 = Fighter(2,700,450,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS)


#game loop
run = True
while run:

    clock.tick(FPS)
    #draw nack ground
    draw_bg()
    
    #show player stats
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,860,20)
    draw_text("Player 1: " + str(score[0]),score_font,RED,20,60)
    draw_text("Player 2: " + str(score[1]),score_font,RED,860,60)

    #update count down
    if intro_count<=0:
    #move fighters
        fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2,round_over)
        fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1,round_over)
    else:
        #display count timer
        draw_text(str(intro_count),count_font,RED,SCREEN_WIDTH/2,SCREEN_HEIGHT/3)
        #update count timer
        if(pygame.time.get_ticks()-last_count_update>=1000):
            intro_count-=1
            last_count_update=pygame.time.get_ticks()



    #update fighters
    fighter_1.update()
    fighter_2.update()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over==False:
        if fighter_1.alive==False:
            score[1]+=1
            round_over=True
            round_over_time=pygame.time.get_ticks()
        elif fighter_2.alive==False:
            score[0]+=1
            round_over=True
            round_over_time=pygame.time.get_ticks()
    else:
        #display victory
        screen.blit(victory_img,(SCREEN_WIDTH/2.5,SCREEN_HEIGHT/2))
        if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
            round_over=False
            intro_count=3
            fighter_1 = Fighter(1,200,450,False,HERO_DATA,hero_sheet,WIZARD_ANIMATION_STEPS)
            fighter_2 = Fighter(2,700,450,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS)

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    #update display
    pygame.display.update()

#exit pygame
pygame.quit()



