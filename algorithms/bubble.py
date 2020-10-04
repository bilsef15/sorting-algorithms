import swap


def bubbleSort(data: list) -> list:
    length = len(data)
    for i in range (0, length-1):
        currIndex = 0
        while (currIndex < length - i - 1):
            print(data)
            if (data[currIndex] > data[currIndex+1]):
                data = swap.swap(data, currIndex, currIndex+1)
            currIndex += 1
    return data