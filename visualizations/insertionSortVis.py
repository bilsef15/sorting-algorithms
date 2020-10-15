
import pygame
import tools.tools as tools
import random

class insertionSortVis:
    
    def __init__(self, sc: pygame.display, numItems: int):
        self._length = numItems
        self._screen = sc
        self._data = []
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        self._rectWidth = self._screenWidth // self._length
        self._rectHeightUnit = (0.8 * self._screenHeight) // 1000
        
        self._font = pygame.font.SysFont("comicsans", 26)
        self._sortName = self._font.render("Insertion Sort", True, (127,127,127))
        
        for i in range(0, self._length-1): 
            self._data.append(random.randint(1,1000))
        
    def sort(self):
        for i in range(1, len(self._data)):
            self._key = i
            while (self._key >= 1) and (self._data[self._key-1] > self._data[self._key]):
                self._data = tools.swap(self._data, self._key, self._key-1)
                self._key-=1
                self.__updateImage()
        
    def __updateImage(self):
        self._screen.fill((0,0,0))
        
        self._screen.blit(self._sortName, (10, 10))
        
        for i in range(0, self._length-1):
            pygame.draw.rect(self._screen, (127,127,127), [i*self._rectWidth, self._screenHeight - self._data[i] // 2, self._rectWidth, self._data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
