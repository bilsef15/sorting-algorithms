
import pygame
import tools.tools as tools

class bubbleSortVis:
    
    def __init__(self, sc, numItems):
        self._length = numItems
        self._screen = sc
        self._data = []
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        self._rectWidth = self._screenWidth // numItems
        
        self._font = pygame.font.SysFont("comicsans", 26)
        self._sortName = self._font.render("Bubble Sort", True, (127,127,127))
        
        self._data = tools.randomList(numItems)
        
    def sort(self):
        for i in range (0, len(self._data)-1):
            self._currIndex = 0
            while (self._currIndex < len(self._data) - i - 1): 
                if (self._data[self._currIndex] > self._data[self._currIndex+1]):
                    self._data = tools.swap(self._data, self._currIndex, self._currIndex+1)
                    self.__updateImage()
                self._currIndex += 1
        
    def __updateImage(self):
        self._screen.fill((0,0,0))
        
        self._screen.blit(self._sortName, (10, 10))
        
        for i in range(0, self._length-1):
            pygame.draw.rect(self._screen, (127,127,127), [i*self._rectWidth, self._screenHeight - self._data[i] // 2, self._rectWidth, self._data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
