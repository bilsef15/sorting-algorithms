'''Implementation of the selection sort algorithm.'''

import tools.toolFunctions as tools

def selectionSort(data: list) -> list:
    '''
    Sorts the list via selection sort.

    Parameters
    ----------
    data : list
        The list to be sorted.

    Returns
    -------
    list
        The sorted list.

    '''
    for i in range(0, len(data)-1):
        minIndex = i 
        for j in range(i+1, len(data)-1):
            if (data[j] < data[minIndex]):
                minIndex = j
        tools.swap(data, minIndex, i)
    return data