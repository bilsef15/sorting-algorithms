# insertion sorting algorithm
import swap

def insertionSort(data: list) -> list:
    for i in range(1, len(data)):
        key = i
        while (key >= 1) and (data[key-1] > data[key]):
            data = swap.swap(data, key, key-1)
            key-=1
    return data
        
