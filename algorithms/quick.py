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
    
def quickSort(data: list, low: int, high: int) -> list:
    '''
    Sorts the list via quicksort.

    Parameters
    ----------
    data : list
        The list to be sorted.
    low : int
        Starting index.
    high : int
        Ending index.

    Returns
    -------
    data : list
        The sorted list from low to high.

    '''
    if low < high:
        part = partition(data, low, high)
        quickSort(data, low, part-1)
        quickSort(data, part+1, high)
    return data