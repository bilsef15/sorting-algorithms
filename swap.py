#swap

def swap(data: list, index1: int, index2: int) -> list:
    data[index1], data[index2] = data[index2], data[index1]
    return data
