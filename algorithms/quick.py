import tools.swap as sw


def partition(data: list, low: int, high: int):
    pivot = data[high]
    i = low-1
    for j in range(low, high):
        if (data[j] < pivot):
            i+=1
            sw.swap(data, i, j)
    sw.swap(data, i+1, high)
    return i+1
    
def quickSort(data: list, low: int, high: int):
    if low < high:
        pivot = partition(data, low, high)
        print(f"Pivot: {pivot}   High: {high}   Low: {low}")
        print(data)
        quickSort(data, low, pivot-1)
        quickSort(data, pivot+1, high)
    return data