
import pygame
import tools.tools as tools
import random

class quickSortVis:
    
    def __init__(self, sc, numItems):
        self._length = numItems
        self._screen = sc
        self._data = []
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        self._rectWidth = self._screenWidth // numItems
        
        self._font = pygame.font.SysFont("comicsans", 26)
        self._sortName = self._font.render("Quick Sort", True, (127,127,127))
        
        for i in range(0, self._length-1): 
            self._data.append(random.randint(1,1000))
        
    def sort(self):
        self.quickSort(self._data, 0 , len(self._data)-1)

 
    def partition(self, data: list, low: int, high: int):
            pivot = data[high]
            i = low - 1
            for j in range(low, high):
                if (data[j] < pivot):
                    i+=1
                    tools.swap(data, i, j)
                    self.__updateImage(data)
            tools.swap(data, i+1, high)
            self.__updateImage(data)
            return i+1
    
    def quickSort(self, data: list, low: int, high: int):
        if low < high:
            pivot = self.partition(data, low, high)
            self.quickSort(data, low, pivot-1)
            self.quickSort(data, pivot+1, high)
   

 
    def __updateImage(self, data):
        self._screen.fill((0,0,0))
        
        self._screen.blit(self._sortName, (10, 10))
        
        for i in range(0, len(data)-1):
            pygame.draw.rect(self._screen, (127,127,127), [i*self._rectWidth, self._screenHeight - data[i] // 2, self._rectWidth, data[i] // 2] )
        pygame.display.update()
        
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
