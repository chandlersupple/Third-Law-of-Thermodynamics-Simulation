import sys        
import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,500))        # Change parameters to extend
pygame.display.set_caption('Crystaline Structure, Third Law of Thermodyanmics')

clock = pygame.time.Clock()

degree = u'\N{DEGREE SIGN}'
font = pygame.font.SysFont("monospace", 20, bold = True)
purple = (171,0,255)
black = (0,0,0)
white = (255,255,255)

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        x, y = pygame.mouse.get_pos()

        ran = int(round((x/50), 0))
        temp = str((x*2)-40)
        if (int(temp) < 0):
            temp = '0'

        screen.fill(black)

        for i in range(0, 20):       # If you changed the screen size, modify the nested for loops (below) accordingly
            j = 0
            for j in range(0, 20):
                x_ = ((j*25)+random.randint((-ran), (ran))+8)
                y_ = ((i*25)+random.randint((-ran), (ran))+8)
                pygame.draw.rect(screen, purple, (x_, y_, 10,10), 2)

        pygame.draw.rect(screen, black, (185, 12, 300, 60), 0)

        label = font.render("Temperature (K%s) = %s" %(degree, temp), 4, (225,255,255))
        screen.blit(label, (205, 32))

        pygame.display.flip()
        clock.tick(30)       # Modify the frame rate to slow down, or speed up the simulation

except:
    print('Sorry, but it looks like an error has occured.')
