
import random
import insertion
import swap

data = []
for i in range(0,30):
    n = random.randint(1,1000)
    data.append(n)

print(data)
print(insertion.insertionSort(data))


