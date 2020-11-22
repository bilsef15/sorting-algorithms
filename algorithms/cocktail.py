'''Implementation of cocktail sort algorithm'''

import tools.toolFunctions as tools

def cocktailSort(data: list) -> list():
    '''
    This implements cocktail sort.

    Parameters
    ----------
    data : list
        This takes the list to be sorted.

    Returns
    -------
    list()
        This returns the sorted list.

    '''
    #Since range is exclusive, initial values are 1 off respectively
    start = -1
    end = len(data)
    
    while (end > start):
        
        #the forward pass
        for index in range(start, end-1):
            if (data[index] > data[index+1]):
                tools.swap(data, index, index+1)
        end-=1
        #the backwards pass
        for index in range(end, start, -1):
            if (data[index] < data[index-1]):
                tools.swap(data, index, index-1)
        start+=1
    return data
