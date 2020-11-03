'''
Sort Menu is a graphical menu based driver for sort visualizer.
'''
import pygame
import tools.menuObjects as mo

class Menu:
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
    
    def __init__(self, sc: pygame.surface):

        self._buttons = []
        self._text = [] #[Name, Rect]...
        self._titleFont = pygame.font.SysFont("comicsans", 36)
            
        self._screen = sc
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
    
    def _draw(self):
        '''
        This draws the buttons contained in the list.

        Returns
        -------
        None.

        '''
        for text in self._text:
            self._screen.blit(text[0], text[1])
            
        for button in self._buttons:
            button.draw(self._screen)
    
    def _wereButtonsClicked(self):
        '''
        This checks whether a button in the list was clicked and runs the
        appropriate function.

        Returns
        -------
        None.

        '''
        for button in self._buttons:
            button.wasClicked()
            
    def addButton(self, text: str, top: float, left: float, width: float, height: float, func, buttonColor: tuple=(127,127,127), textColor: tuple=(255,255,255), font="comicsans", pt=26):
        newButton = mo.Button(text, top, left, width, height, func, buttonColor, textColor, font, pt)
        self._buttons.append(newButton)
    
    def addText(self, text, top: float, left: float, width: float, height: float):
        text = self._titleFont.render(text, True, (255,255,255))
        top = top*self._screenHeight
        left = left*self._screenWidth
        width = width*self._screenWidth
        height = height*self._screenWidth
        titleRect = pygame.Rect(top, left, width, height)
        titleRect = text.get_rect(center = titleRect.center)
        self._text.append([text, titleRect])
        
    def run(self):
        '''
        This runs the sortMenu object.

        Returns
        -------
        None.

        '''
        self._screen.fill((0,0,0))
        self._draw()
        pygame.display.update()
        self._wereButtonsClicked()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()