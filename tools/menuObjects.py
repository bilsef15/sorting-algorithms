'''
menuObjects.py contains the classes contained in menu.py.
'''


import pygame

def doNothing():
    '''
    This function does nothing. It is used as a default for the interactive
    menu objects.

    Returns
    -------
    None.

    '''
    return

class Button:
    
    def __init__(self, text: str, left: float, top: float, width: 
                 float, height: float, func, buttonColor: tuple, 
                 textColor: tuple, font: str, pt: int):
        
        self._buttonColor = buttonColor
        self._textColor = textColor
        
        self._font = pygame.font.SysFont(font, pt)
        self._text = self._font.render(text, True, self._textColor)
        
        
        self._function = func
        
        screenWidth = pygame.display.get_surface().get_width()
        screenHeight = pygame.display.get_surface().get_height()
        top = top*screenHeight
        left = left*screenWidth
        width = width*screenWidth
        height = height*screenWidth
        self._buttonRect = pygame.Rect(left,top,width,height)
        self._nameRect = self._text.get_rect(center=self._buttonRect.center)
        
    def draw(self, screen: pygame.surface):
        '''
        This draws the button to the provided surface.

        Parameters
        ----------
        screen : pygame.surface
            The surface the button will be drawn to.

        Returns
        -------
        None.

        '''
        pygame.draw.rect(screen, self._buttonColor, self._buttonRect)
        screen.blit(self._text, self._nameRect)
        
    def wasClicked(self):
        '''
        This checks if the button was clicked and runs the button's
        function if it was.

        Returns
        -------
        None.

        '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((click[0] == 1) and 
            (self._buttonRect.left < mouse[0] < self._buttonRect.right) and 
            (self._buttonRect.top < mouse[1] < self._buttonRect.bottom)):
            self._function()
            
class Text:
    
    def __init__(self, text, left: float, top: float, width:
                 float, height: float, func, textColor: tuple,
                 font: str, pt: int):
        
        self._textColor = textColor
        
        self._font = pygame.font.SysFont(font, pt)
        self._text = self._font.render(text, True, self._textColor)
        
        self._function = func
        
        screenWidth = pygame.display.get_surface().get_width()
        screenHeight = pygame.display.get_surface().get_height()
        
        top = top*screenHeight
        left = left*screenWidth
        width = width*screenWidth
        height = height*screenWidth
        
        self._textRect = titleRect = pygame.Rect(left, top, width, height)
        self._textRect = self._text.get_rect(center = titleRect.center)
        
    def draw(self, screen: pygame.surface):
        '''
        This blits the text to the provided surface.

        Parameters
        ----------
        screen : pygame.surface
            The surface to be blitted to.

        Returns
        -------
        None.

        '''
        screen.blit(self._text, self._textRect)
        
    def wasClicked(self):
        '''
        This checks if the text rectange was clicked and runs the text's
        function if it was clicked.

        Returns
        -------
        None.

        '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((click[0] == 1) and 
            (self._textRect.left < mouse[0] < self._textRect.right) and 
            (self._textRect.top < mouse[1] < self._textRect.bottom)):
            self._function()