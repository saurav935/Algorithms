
'''
1. Time complexity:
Worst: O(n^2)
Best: O(n^2)

2. Unstable algorithm

3. Space complexity: O(1)
'''


def insertion_sort(arr):
    n = len(arr)
    for i in range(0,n):
        last = n-i-1
        maxIndex = getMaxIndex(arr,0,last)
        swap(arr,maxIndex,last)

    return arr

def getMaxIndex(arr,start,last):
    return arr.index(max(arr[start:last+1]))

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


    
