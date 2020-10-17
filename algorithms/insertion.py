'''Implementation of insertion sort algorithm'''

import tools.tools as tools

def insertionSort(data: list) -> list:
    '''
    Sorts the list via insertion sort.

    Parameters
    ----------
    data : list
        The list to be sorted.

    Returns
    -------
    list
        The sorted list.

    '''
    for i in range(1, len(data)):
        key = i
        while (key >= 1) and (data[key-1] > data[key]):
            data = tools.swap(data, key, key-1)
            key-=1
    return data
        
