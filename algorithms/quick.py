'''Implementation of quick sort'''
import tools.tools as tools

def partition(data: list, low: int, high: int) -> int:
    '''
    The partition function of quick sort. It uses the 'high' element as
    the pivot. It rearranges the array so that all values to the left (starting
    from low) are less than the pivot and all values to the right are greater
    (up to high.)
    
    Parameters
    ----------
    data : list
        The list to be partitioned.
    low : int
        The lowest index to be affected.
    high : int
        The highest index to be affected.

    Returns
    -------
    int
        The index of the pivot value.

    '''
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if (data[j] < pivot):
            i+=1
            tools.swap(data, i, j)
    tools.swap(data, i+1, high)
    return i+1
    
def quickSort(data: list, low: int = 0, high: int = None) -> list:
    '''
    This sorts the list via quick sort.

    Parameters
    ----------
    data : list
        The list to be acted on.
    low : int, optional
        The lower index of the list to be sorted. The default is 0.
    high : int, optional
        The higher index of the list to be sorted. The default is the length of the given list.

    Returns
    -------
    list
        The sorted list from low to high.

    '''
    
    #Handles the default value. Since default high is len(data) and data is an
    #arguement. One must use an if-check.
    if (high == None):
        high = len(data)-1
        
    if low < high:
        part = partition(data, low, high)
        quickSort(data, low, part-1)
        quickSort(data, part+1, high)
    return data
