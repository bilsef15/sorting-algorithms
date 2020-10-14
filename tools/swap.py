#it swaps two elements in a list and returns the list
#This is trivial in python, but functions for this are often included in
#more strongly typed languages

def swap(data: list, index1: int, index2: int) -> list:
    data[index1], data[index2] = data[index2], data[index1]
    return data
