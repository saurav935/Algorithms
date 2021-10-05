

def InsertionSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        j = i+1
        while j > 0:
            if arr[j] < arr[j-1]:
                swap(arr,j,j-1)
            else:
                break
            j -= 1
    return arr


def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [56,18]
print(InsertionSort(arr))