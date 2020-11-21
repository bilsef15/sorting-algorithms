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

        self._elements = []
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
        for element in self._elements:
            element.draw(self._screen)
    
    def _wereElementsClicked(self):
        '''
        This checks whether a button in the list was clicked and runs the
        appropriate function.

        Returns
        -------
        None.

        '''
        for element in self._elements:
            element.wasClicked()
            
    def addButton(self, text: str, left: float, top: float, width: float, height: float, func=mo.doNothing, buttonColor: tuple=(127,127,127), textColor: tuple=(255,255,255), font: str="comicsans", pt=26):
        newButton = mo.Button(text, left, top, width, height, func, buttonColor, textColor, font, pt)
        self._elements.append(newButton)
    
    def addText(self, text, left: float, top: float, width: float, height: float, func=mo.doNothing, textColor: tuple=(255,255,255), font: str="comicsans", pt=32):
        newText = mo.Text( text, left, top, width, height, func, textColor, font, pt)
        self._elements.append(newText)
        
    def doNothing(self):
        return
        
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
        self._wereElementsClicked()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()