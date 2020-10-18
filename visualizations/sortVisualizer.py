import pygame
import tools.tools as tools

class sortVisualizer:
    
    def __init__(self, sc, numItems):
        self._length = numItems
        self._screen = sc
        self._data = tools.randomList(numItems)
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        self._rectWidth = self._screenWidth // numItems
        
        self._font = pygame.font.SysFont("comicsans", 26)
        self._sortName = ""
        
    def newList(self):
        self._data = tools.randomList(self._length)
        
    def __updateImage(self):
        self._screen.fill((0,0,0))
        
        self._screen.blit(self._sortNameRendered, (10, 10))
        
        for i in range(0, self._length-1):
            pygame.draw.rect(self._screen, (127,127,127), [i*self._rectWidth, self._screenHeight - self._data[i] // 2, self._rectWidth, self._data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def __renderName(self, name):
        self._sortName = name
        self._sortNameRendered = self._font.render(self._sortName, True, (127,127,127))

    
    def bubbleSort(self):
        self.__renderName("Bubble Sort")
        for i in range (0, len(self._data)-1):
            self._currIndex = 0
            while (self._currIndex < len(self._data) - i - 1): 
                if (self._data[self._currIndex] > self._data[self._currIndex+1]):
                    self._data = tools.swap(self._data, self._currIndex, self._currIndex+1)
                    self.__updateImage()
                self._currIndex += 1

    
    def selectionSort(self):
        self.__renderName("Selection Sort")
        for i in range(0, len(self._data)-1):
            self._minIndex = i
            for j in range(i+1, len(self._data)-1):
                if (self._data[j] < self._data[self._minIndex]):
                    self._minIndex = j
            tools.swap(self._data, self._minIndex, i)
            self.__updateImage()
                
            
    def insertionSort(self):
        self.__renderName("Insertion Sort")
        for i in range(1, len(self._data)):
            self._key = i
            while (self._key >= 1) and (self._data[self._key-1] > self._data[self._key]):
                self._data = tools.swap(self._data, self._key, self._key-1)
                self._key-=1
                self.__updateImage()
                
    
    def quickSort(self):
        self.__renderName("Quick Sort")
        self.quickSortAlgo(self._data, 0 , len(self._data)-1)

 
    def partition(self, data: list, low: int, high: int):
            pivot = data[high]
            i = low - 1
            for j in range(low, high):
                if (data[j] < pivot):
                    i+=1
                    tools.swap(data, i, j)
                    self.__updateImage()
            tools.swap(data, i+1, high)
            self.__updateImage()
            return i+1
    
    def quickSortAlgo(self, data: list, low: int, high: int):
        if low < high:
            pivot = self.partition(data, low, high)
            self.quickSortAlgo(data, low, pivot-1)
            self.quickSortAlgo(data, pivot+1, high)
                
                
                
                
                
                