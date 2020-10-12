import tools.swap as sw

def selectionSort(data: list) -> list:
    for i in range(0, len(data)-1):
        minIndex = i
        for j in range(i+1, len(data)-1):
            if (data[j] < data[minIndex]):
                minIndex = j
        sw.swap(data, minIndex, i)
        print(data)
    return data