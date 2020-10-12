import pygame
import tools.swap as sw
import random

class selectionSortVis:
    
    def __init__(self, sc, numItems):
        self._length = numItems
        self._screen = sc
        self._data = []
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        self._rectWidth = self._screenWidth // numItems
        
        self._font = pygame.font.SysFont("comicsans", 26)
        self._sortName = self._font.render("Selection Sort", True, (127,127,127))
        
        for i in range(0, self._length-1): 
            self._data.append(random.randint(1,1000))
        
    def sort(self):
        for i in range(0, len(self._data)-1):
            self._minIndex = i
            for j in range(i+1, len(self._data)-1):
                if (self._data[j] < self._data[self._minIndex]):
                    self._minIndex = j
            sw.swap(self._data, self._minIndex, i)
            self._updateImage()
        
    def _updateImage(self):
        self._screen.fill((0,0,0))
        
        self._screen.blit(self._sortName, (10, 10))
        
        for i in range(0, self._length-1):
            pygame.draw.rect(self._screen, (127,127,127), [i*self._rectWidth, self._screenHeight - self._data[i] // 2, self._rectWidth, self._data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
