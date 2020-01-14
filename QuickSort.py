import matplotlib.pyplot as plt
def partition(arr, low, high):
    x_range = list(range(0, len(arr)))
    #print(low, high)
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            if(i!=j):
                plt.bar(x_range, arr)
                plt.pause(0.05)
                plt.clf()
            #print(low, high, i, j)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)





