
import pygame
import visualizerModules.sortMenu as sm


numItems = 75

pygame.init()
screen = pygame.display.set_mode([800,600])

sortMenu = sm.sortMenu(screen, numItems)

while True:
    sortMenu.run()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()