

import pygame
import swap as sw
import random

class insertionSortVis:
    
    def __init__(self, sc: pygame.display, numItems: int):
        self.length = numItems
        self.screen = sc
        self.data = []
        self.screenWidth = pygame.display.get_surface().get_width()
        self.screenHeight = pygame.display.get_surface().get_height()
        self.rectWidth = self.screenWidth // self.length
        self.rectHeightUnit = (0.8 * self.screenHeight) // 1000
        for i in range(0, self.length-1): 
            self.data.append(random.randint(1,1000))
        
    def sort(self):
        for i in range(1, len(self.data)):
            self.key = i
            while (self.key >= 1) and (self.data[self.key-1] > self.data[self.key]):
                self.data = sw.swap(self.data, self.key, self.key-1)
                self.key-=1
                self.__updateImage()
        
    def __updateImage(self):
        self.screen.fill((0,0,0))
        for i in range(0, self.length-1):
            pygame.draw.rect(self.screen, (127,127,127), [i*self.rectWidth, self.screenHeight - self.data[i] // 2, self.rectWidth, self.data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
