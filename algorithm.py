import algorithms.selection as selection
import algorithms.quick as quick
import random

data = []

for i in range(0, 20): 
    data.append(random.randint(1,1000))
print (data) 
print(quick.quickSort(data, 0, len(data)-1))
