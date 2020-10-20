
import pygame
import visualizerModules.sortVisualizer as sv

class sortMenu:
    
    def __init__(self, sc: pygame.surface, numItems: int):
        self._sortVisualizer = sv.sortVisualizer(sc, numItems)
        self._buttons = [["Bubble Sort", self.__bubbleSort],
                         ["Selection Sort", self.__selectionSort],
                         ["Insertion Sort", self.__insertionSort],
                         ["Quick Sort", self.__quickSort]]
        self._font = pygame.font.SysFont("comicsans", 26)
        self._fontTitle = pygame.font.SysFont("comicsans", 36)
            
        self._screen = sc
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        
        self._buttonWidth = self._screenWidth // 2
        self._buttonHeight = (self._screenHeight) // (len(self._buttons) + 1)
        
        self._title = self._fontTitle.render("Sorting Algorithms", True, (255, 255, 255))
        self._titleRect = self._title.get_rect(center=(self._screenWidth // 2, self._buttonHeight // 2))
        
        for i in range(0, len(self._buttons)):
            button = self._buttons[i]
            button[0] = self._font.render(button[0], True, (255,255,255))
            button.append(self._screenWidth // 4)
            button.append(self._buttonHeight * i)

    def __bubbleSort(self):
        self._sortVisualizer.newList()
        self._sortVisualizer.bubbleSort()
    
    def __selectionSort(self):
        self._sortVisualizer.newList()
        self._sortVisualizer.selectionSort()
        
    def __insertionSort(self):
        self._sortVisualizer.newList()
        self._sortVisualizer.insertionSort()
    
    def __quickSort(self):
        self._sortVisualizer.newList()
        self._sortVisualizer.quickSort()
    
    def __drawButtons(self):
        for button in self._buttons:
            buttonRect = pygame.Rect(button[2], button[3] + self._buttonHeight, self._buttonWidth, self._buttonHeight - 20)
            nameRect = button[0].get_rect(center=(button[2] + (self._buttonWidth // 2), button[3] + self._buttonHeight + (self._buttonHeight // 2)))
            pygame.draw.rect(self._screen, (127,127,127), buttonRect)
            self._screen.blit(button[0], nameRect)
    
    def __wereButtonsClicked(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        for button in self._buttons:
            if (click[0] == 1) and (button[2] < mouse[0] < (button[2] + self._buttonWidth)) and ((button[3] + self._buttonHeight) < mouse[1] < (button[3] + self._buttonHeight + self._buttonHeight - 20)):
                button[1]()
                
            
        
    def run(self):
        self._screen.fill((0,0,0))
        self.__drawButtons()
        self._screen.blit(self._title, self._titleRect)
        pygame.display.update()
        self.__wereButtonsClicked()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()