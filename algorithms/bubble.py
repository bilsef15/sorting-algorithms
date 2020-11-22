'''Implementation of bubble sort'''

import tools.toolFunctions as tools

def bubbleSort(data: list) -> list:
    '''
    Sorts the given list using bubble sort.

    Parameters
    ----------
    data : list
        The list to be sorted.

    Returns
    -------
    list
        The sorted list.

    '''
    length = len(data)
    for i in range (0, length-1):
        currIndex = 0
        while (currIndex < length - i - 1):
            if (data[currIndex] > data[currIndex+1]):
                data = tools.swap(data, currIndex, currIndex+1)
            currIndex += 1
    return data