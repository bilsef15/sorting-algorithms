import pygame
import tools.menu as menu


def clicked():
    
    position = pygame.mouse.get_pos()
    print(f'You clicked a button! x={position[0]}, y={position[1]}')

pygame.init()
screen = pygame.display.set_mode([800,800])

mainMenu = menu.Menu(screen)

mainMenu.addText("Test Title 1", 0.0, 0.0, 0.2, 0.1)
mainMenu.addText("Test Title 2", 0.4, 0.0, 0.2, 0.1)
mainMenu.addText("Test Title 3", 0.8, 0.0, 0.2, 0.1)

for x in range(0, 10):
    for y in range(1, 10):
        mainMenu.addButton(f'Test {x + y*10}', x/10, y/10, 0.08, 0.08, clicked, (x*5, y*5, x*y + 100), (y*5, x*5, x*y))
        
while True:
    mainMenu.run()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        
