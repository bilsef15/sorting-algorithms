'''
This contains the sortVisualizer class which displays sorting algorithms via pygame.
'''

import pygame
import tools.tools as tools

class sortVisualizer:
    '''
    It contains sorting algorithms and a means to display them.
    
    Variables
    ---------
    _data: list
        The list of integers that can be sorted.
    _length: int
        The length of the list of integers.
    _screen: pygame.surface
        The surface that will be drawn to.
    _screenWidth
        The width of the pygame window.
    _screenHeight
        The height of the pygame window.
    _rectWidth
        The width of the bar that represents an integer.
    _font
        The font text will be displayed in.
    _sortName
        The name of the given sort being run.
    _sortNameRendered
        The _sortName rendered so that it can be blitted.
        
    Methods
    -------
    __init__(self, sc: pygame.surface, numItems: int) -> sortVisualizer
    newList(self)
    _updateImage(self)
    _renderName(self, name)
    newList(self, length: int = None)
    bubbleSort(self)
    selectionSort(self)
    insertionSort(self)
    quickSort(self)
    partition(self, data: list, low: int, high: int)
    _quickSortAlgo(self, data: list, low: int, high: int):
    shellSort(self)
    
    '''
    
    def __init__(self, sc: pygame.surface, numItems: int):
        '''
        This instantiates a sortVisualizer object.
        
        Parameters
        ----------
        sc : pygame.surface
            The surface that will be drawn to.
        numItems : int
            The number of items for the internal list.
        '''
        self._length = numItems
        self._screen = sc
        self._data = tools.randomList(numItems)
        self._screenWidth = pygame.display.get_surface().get_width()
        self._screenHeight = pygame.display.get_surface().get_height()
        self._rectWidth = (self._screenWidth - 40) / numItems
        
        self._font = pygame.font.SysFont("comicsans", 26)
        self._sortName = ""
    
    
    def newList(self, length: int = None):
        '''
        newList generates a new random list of supplied length. 

        Parameters
        ----------
        length : int, optional
            This sets the length of the new list. The default is the previous
            length.

        Returns
        -------
        None.

        '''
        if (length != None) and (length >= 10) and (length <= 500):
            self._length = length
        self._data = tools.randomList(self._length)
        
    def _updateImage(self):
        '''
        This updates the window with the current representation of the list.

        Returns
        -------
        None.

        '''
        self._screen.fill((0,0,0))
        
        self._screen.blit(self._sortNameRendered, (10, 10))
        
        for i in range(0, self._length-1):
            pygame.draw.rect(self._screen, (127,127,127), [i*self._rectWidth + 20, self._screenHeight - self._data[i] // 2, self._rectWidth - 3, self._data[i] // 2] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def _renderName(self, name: str):
        '''
        This renders the supplied text with the given font.

        Parameters
        ----------
        name : str
            The name of the sorting algorithm.

        Returns
        -------
        None.

        '''
        self._sortName = name
        self._sortNameRendered = self._font.render(self._sortName, True, (127,127,127))

    
    def bubbleSort(self):
        '''
        This sorts the internal list via bubble sort.

        Returns
        -------
        None.

        '''
        self._renderName("Bubble Sort")
        for i in range (0, len(self._data)-1):
            currIndex = 0
            while (currIndex < len(self._data) - i - 1): 
                if (self._data[currIndex] > self._data[currIndex+1]):
                    self._data = tools.swap(self._data, currIndex, currIndex+1)
                    self._updateImage()
                currIndex += 1

    
    def selectionSort(self):
        '''
        This sorts the internal list via selection sort.

        Returns
        -------
        None.

        '''
        self._renderName("Selection Sort")
        for i in range(0, len(self._data)-1):
            minIndex = i
            for j in range(i+1, len(self._data)-1):
                if (self._data[j] < self._data[minIndex]):
                    minIndex = j
            tools.swap(self._data, minIndex, i)
            pygame.time.wait(50)
            self._updateImage()
                
            
    def insertionSort(self):
        '''
        This sorts the internal list via insertion sort.

        Returns
        -------
        None.

        '''
        self._renderName("Insertion Sort")
        for i in range(1, len(self._data)):
            key = i
            while (key >= 1) and (self._data[key-1] > self._data[key]):
                self._data = tools.swap(self._data, key, key-1)
                key-=1
                self._updateImage()
                
    
    def quickSort(self):
        '''
        This sorts the intenral list via quick sort. It is a public driver
        method so that _renderName is called once rather than everytime
        quickSort is called.

        Returns
        -------
        None.

        '''
        self._renderName("Quick Sort")
        self._quickSortAlgo(self._data, 0 , len(self._data)-1)

 
    def partition(self, data: list, low: int, high: int) -> int:
        '''
        This is th partitioning function for quicksort. It places all values
        higher than the pivot (high index) to the right of
        the pivot, and it places the lower values to the left of the pivot.

        Parameters
        ----------
        data : list
            The list to be acted on.
        low : int
            The lower index of the sub list to be sorted.
        high : int
            The higher index of the sub list to be sorted.

        Returns
        -------
        int
            The new pivot point.

        '''
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if (data[j] < pivot):
                i+=1
                tools.swap(data, i, j)
                pygame.time.wait(15)
                self._updateImage()
        tools.swap(data, i+1, high)
        self._updateImage()
        return i+1
    
    def _quickSortAlgo(self, data: list, low: int, high: int):
        '''
        The actual quick sort algorithm.

        Parameters
        ----------
        data : list
            The list to be acted on.
        low : int
            The lower index of the sub list to be sorted.
        high : int
            The higher index of the sub list to be sorted.

        Returns
        -------
        None.

        '''
        pygame.time.wait(20)
        if low < high:
            pivot = self.partition(data, low, high)
            self._quickSortAlgo(data, low, pivot-1)
            self._quickSortAlgo(data, pivot+1, high)

    def shellSort(self):
        '''
        This sorts the internal list via shell sort.
    
        Returns
        -------
        None.
    
        '''
        self._renderName("Shell Sort")
        interval = len(self._data)//2
        while interval > 0:
            for i in range(interval, len(self._data)):
                firstDatum = self._data[i]
                compareIndex = i
                while compareIndex >= interval and self._data[
                        compareIndex-interval] > firstDatum:
                    self._data[compareIndex] = self._data[compareIndex - interval]
                    self._updateImage()
                    compareIndex -= interval
                self._data[compareIndex] = firstDatum
                pygame.time.wait(10)
                self._updateImage()
            interval //= 2
             
                
                
                
                
                