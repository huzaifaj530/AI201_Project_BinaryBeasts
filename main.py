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

#background image
bg_image=pygame.image.load("assets/images/background/background.gif").convert_alpha()#load to memory


#function for drawing image
def draw_bg():
    scaled_bg=pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#create two instances of fighters
fighter_1 = Fighter(200,450)
fighter_2 = Fighter(700,450)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw nack ground
    draw_bg()
    
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



