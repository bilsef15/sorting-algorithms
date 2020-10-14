#implements selection sort

#selection sort divides the list into a sorted and unsorted part
#it finds the next lowest value and places it at the end of the sorted list

#including the swap function
import tools.swap as sw

def selectionSort(data: list) -> list:
    #loop from left to right
    for i in range(0, len(data)-1):
        minIndex = i #assume first index of unsorted array is minimum
        #loop from left side of unsorted list to end of sorted list
        for j in range(i+1, len(data)-1):
            #swap the lowest value in unsorted with the end of the sorted list
            if (data[j] < data[minIndex]):
                minIndex = j
        sw.swap(data, minIndex, i)
        print(data)
    return data