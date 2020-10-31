''' Implementation of Shell Sort Algorithm'''

def shellSort(data: list) -> list:
    '''
    Implementation of Shell Sort

    Parameters
    ----------
    data : list
        The unsorted list.

    Returns
    -------
    list
       The sorted List.

    '''
    interval = len(data)//2
    while interval > 0:
        for i in range(interval, len(data)):
            firstDatum = data[i]
            compareIndex = i
            while compareIndex >= interval and data[
                    compareIndex-interval] > firstDatum:
                data[compareIndex] = data[compareIndex - interval]
                compareIndex -= interval
            data[compareIndex] = firstDatum
        interval //= 2
    return data