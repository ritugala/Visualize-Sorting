from Bubble import bubble
import random
from Merge import mergeSort
from QuickSort import quickSort
from Selection import selection
import matplotlib.pyplot as plt

x = input("Enter what sorting you want to visualize: ")
n = int(input("Enter size of array: "))
A = random.sample(range(1, n+1), n)


if x=='b':
    bubble(A)
elif x=='m':
    mergeSort(A, 0, n-1)
elif x=='q':
    quickSort(A, 0, n-1)
elif x=='s':
    selection(A)

plt.bar(list(range(0, len(A))), A)
plt.pause(0.1)
plt.close()