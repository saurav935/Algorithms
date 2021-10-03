
'''
1. Time cpmplexity:
Best case: O(n)
Worst case: O(n^2)

2. Space complexity: O(1)

3. It is a STABLE sorting algorithm
'''



def bubble_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    for i in range(0,n):
        swapped = False
        for j in range(1,n-i):
            if arr[j-1] > arr[j]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                swapped = True

        if not swapped:
            break

    return arr


arr = [3,1,5,4,2]
print(bubble_sort(arr))
