
import pygame
import visualizerModules.sortVisualizer as SV
import tools.menu as menu


def exitVisualizer():
    pygame.quit()

numItems = 100

pygame.init()
screen = pygame.display.set_mode([800,800])

sv = SV.sortVisualizer(screen, numItems)

mainMenu = menu.Menu(screen)
mainMenu.addText("Sorting Algorithms", 0.344, 0.05, 0.313, 0.1)
mainMenu.addButton("Bubble Sort", 0.02, 0.2, 0.313, 0.1, sv.bubbleSort)
mainMenu.addButton("Insertion Sort", 0.344, 0.2, 0.313, 0.1, sv.insertionSort)
mainMenu.addButton("Quick Sort", 0.667, 0.2, 0.313, 0.1, sv.quickSort)
mainMenu.addButton("Selection Sort", 0.02, 0.4, 0.313, 0.1, sv.selectionSort)
mainMenu.addButton("Shell Sort", 0.344, 0.4, 0.313, 0.1, sv.shellSort)
mainMenu.addButton("Cocktail Sort", 0.667, 0.4, 0.313, 0.1, sv.cocktailSort)
mainMenu.addButton("Exit", 0.344, 0.8, 0.313, 0.1, exitVisualizer)

while True:
    mainMenu.run()
    sv.newList()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()