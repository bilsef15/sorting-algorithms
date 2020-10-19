
import pygame
import visualizations.sortVisualizer as sortVisualizer


numItems = 150

pygame.init()
screen = pygame.display.set_mode([800,600])

algoVisualizer = sortVisualizer.sortVisualizer(screen, numItems)

algoVisualizer.newList()
algoVisualizer.quickSort()

algoVisualizer.newList()
algoVisualizer.insertionSort()

algoVisualizer.newList()
algoVisualizer.bubbleSort()

algoVisualizer.newList()
algoVisualizer.selectionSort()

pygame.quit()