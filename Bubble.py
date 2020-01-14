import matplotlib.pyplot as plt

def swap(s1, s2):
    return s2, s1

def bubble(A):
    x_value = list(range(len(A)))
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if(A[i]>A[j]):
                A[i], A[j] = swap(A[i], A[j])
                plt.bar(x_value, A)
                #plt.xticks(A)
                plt.pause(0.005)
                plt.clf()



