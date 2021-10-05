
'''
Time complexity - O(n)
Space complexity - O(1)

NOTE: Can only be applied when the array is in the range 1 to n, n is the size of the array

'''



def CyclicSort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]-1
        if arr[i] != arr[correct]:
            swap(arr,i,correct)
        else:
            i += 1


def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp



