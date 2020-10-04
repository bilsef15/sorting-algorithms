
import pygame
import swap as sw
import random

class bubbleSortVis:
    
    def __init__(self, sc, numItems):
        self.__length = numItems
        self.__screen = sc
        self.__data = []
        self.__screenWidth = pygame.display.get_surface().get_width()
        self.__screenHeight = pygame.display.get_surface().get_height()
        self.__rectWidth = self.__screenWidth // numItems
        
        self.__font = pygame.font.SysFont("comicsans", 26)
        self.__sortName = self.__font.render("Bubble Sort", True, (127,127,127))
        
        for i in range(0, self.__length-1): 
            self.__data.append(random.randint(1,1000))
        
    def sort(self):
        for i in range (0, len(self.__data)-1):
            self.__currIndex = 0
            while (self.__currIndex < len(self.__data) - i - 1):
                self.__updateImage()
                if (self.__data[self.__currIndex] > self.__data[self.__currIndex+1]):
                    self.__data = sw.swap(self.__data, self.__currIndex, self.__currIndex+1)
                self.__currIndex += 1
        
    def __updateImage(self):
        self.__screen.fill((0,0,0))
        
        self.__screen.blit(self.__sortName, (10, 10))
        
        for i in range(0, self.__length-1):
            pygame.draw.rect(self.__screen, (127,127,127), [i*self.__rectWidth, self.__screenHeight - self.__data[i] // 2, self.__rectWidth, self.__data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
