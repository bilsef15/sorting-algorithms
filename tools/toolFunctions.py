'''
This module contains useful functions for developing sorting algorithms.
   
Functions
---------
swap(list, int, int) -> list
randomList(int) -> list
isSorted(list) -> bool
'''

import random

def swap(data: list, index1: int, index2: int) -> list:
    '''
    Returns the list with the data of the two indexes swapped.
    
    Parameters
    ----------
    data : list
        List that will be acted on.
    index1 : int
        First index to be switched.
    index2 : int
        Second index to be switched.

    Returns
    -------
    list
        The list with the values at index1 and index2 swapped.

    '''
    
    data[index1], data[index2] = data[index2], data[index1]
    return data

def randomList(length: int) -> list:
    """
    Returns a given length list of random integers from 0-1000.

    Parameters
    ----------
    length : int
        The length of the random list.

    Returns
    -------
    list
        The list of random integers from 0-1000.

    """
    data = []
    for i in range(0, length): 
        data.append(random.randint(1,1000))
    return data

def isSorted(data: list) -> bool:
    '''
    Returns true if the list is sorted from left to right else returns false.

    Parameters
    ----------
    data : list
        The list to be checked.

    Returns
    -------
    bool
        True if the list is sorted from left to right else it returns false.

    '''
    sort = True
    for i in range(1, len(data)):
        if (data[i] < data[i-1]):
            sort = False
    return sort