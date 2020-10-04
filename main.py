
import pygame
import bubbleSortVis as bubble
import insertionSortVis as insertion

numItems = 100

pygame.init()
screen = pygame.display.set_mode([800,600])

insertionSort = insertion.insertionSortVis(screen, numItems)
insertionSort.sort()

bubbleSort = bubble.bubbleSortVis(screen, numItems)
bubbleSort.sort()

pygame.quit()