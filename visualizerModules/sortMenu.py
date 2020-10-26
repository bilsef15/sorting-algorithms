'''
Sort Menu is a graphical menu based driver for sort visualizer.
'''
import pygame
import visualizerModules.sortVisualizer as sv

class sortMenu:
    '''
    Variables
    ---------
    _sortVisualizer: sortVisualizer
        This contains all the sorts. A sortMenu drives a sortVisualizer.
    _buttons: list
        A list containing all the buttons, location, and
        function.
    _font: pygame.font
       The font of the menu options.
    _fontTitle: pygame.font
        The font of the title.
    _screen: pygame.display
        The pygame window.
    _screenWidth: int
        The width of the pygame screen.
    _screenHeight: int
        The height of the pygame screen.
    _buttonWidth: int
        The width of the buttons.
    _buttonHeight: int
        The height of the buttons.
    _title: str
        The title text.
    _titleRect: pygame.rect
        The rectangle for the title text.
        
    Methods
    ------
    __init__( pygame.surface, int)
    _drawButtons()
    _wereButtonsClicked()
    run()
    '''
    
    def __init__(self, sc: pygame.surface, numItems: int):
        '''
        This builds a sort menu class.
        
        Variables
        ---------
        _sortVisualizer: sortVisualizer
            This contains all the sorts. A sortMenu drives a sortVisualizer.
        _buttons: list
            A list containing all the buttons, location, and
            function.
        _font: pygame.font
            The font of the menu options.
        _fontTitle: pygame.font
            The font of the title.
        _screen: pygame.display
            The pygame window.
        _screenWidth: int
            The width of the pygame screen.
        _screenHeight: int
            The height of the pygame screen.
        _buttonWidth: int
            The width of the buttons.
        _buttonHeight: int
            The height of the buttons.
        _title: str
            The title text.
        _titleRect: pygame.rect
            The rectangle for the title text.

        Parameters
        ----------
        sc : pygame.surface
            DESCRIPTION.
        numItems : int
            DESCRIPTION.

        Returns
        -------
        A sortMenu object.

        '''
        self._sortVisualizer = sv.sortVisualizer(sc, numItems)
        self._buttons = [["Bubble Sort", self._sortVisualizer.bubbleSort],
                         ["Selection Sort", self._sortVisualizer.selectionSort],
                         ["Insertion Sort", self._sortVisualizer.insertionSort],
                         ["Quick Sort", self._sortVisualizer.quickSort]]
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
    
    def _drawButtons(self):
        '''
        This draws the buttons contained in the list.

        Returns
        -------
        None.

        '''
        for button in self._buttons:
            buttonRect = pygame.Rect(button[2], button[3] + self._buttonHeight, self._buttonWidth, self._buttonHeight - 20)
            nameRect = button[0].get_rect(center=(button[2] + (self._buttonWidth // 2), button[3] + self._buttonHeight + (self._buttonHeight // 2)))
            pygame.draw.rect(self._screen, (127,127,127), buttonRect)
            self._screen.blit(button[0], nameRect)
    
    def _wereButtonsClicked(self):
        '''
        This checks whether a button in the list was clicked and runs the
        appropriate function.

        Returns
        -------
        None.

        '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        for button in self._buttons:
            if (click[0] == 1) and (button[2] < mouse[0] < (button[2] + self._buttonWidth)) and ((button[3] + self._buttonHeight) < mouse[1] < (button[3] + self._buttonHeight + self._buttonHeight - 20)):
                self._sortVisualizer.newList()
                button[1]()
        
    def run(self):
        '''
        This runs the sortMenu object.

        Returns
        -------
        None.

        '''
        self._screen.fill((0,0,0))
        self._drawButtons()
        self._screen.blit(self._title, self._titleRect)
        pygame.display.update()
        self._wereButtonsClicked()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()