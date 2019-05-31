import pygame
import random
import os


WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folder

game_folder = os.path.dirname(__file__) #__file__ tracks current file on drive
img_folder = os.path.join(game_folder, "img") #will join IMG to path knows / or \ in different systems




class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #"""self.image = pygame.Surface((50, 50)) 
        #self.image.fill(GREEN)""" #green square

        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert() 
        #convert helps pygame operate easly on drawing (it is faster)
        self.image.set_colorkey(BLACK) #creates image opacity
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed

        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top <200:
            self.y_speed = 5

        if self.rect.left > WIDTH:
            self.rect.right = 0
            


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(GREEN)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()