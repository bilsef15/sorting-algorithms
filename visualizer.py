
import pygame
import visualizations.bubbleSortVis as bubble
import visualizations.insertionSortVis as insertion
import visualizations.selectionSortVis as selection
import visualizations.quickSortVis as quick

numItems = 150

pygame.init()
screen = pygame.display.set_mode([800,600])

quickSort = quick.quickSortVis(screen, numItems)
quickSort.sort()

insertionSort = insertion.insertionSortVis(screen, numItems)
insertionSort.sort()

bubbleSort = bubble.bubbleSortVis(screen, numItems)
bubbleSort.sort()

selectionSort = selection.selectionSortVis(screen, numItems)
selectionSort.sort()

pygame.quit()