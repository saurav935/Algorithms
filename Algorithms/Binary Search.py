

def binary_search(arr,target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        
        # find the middle element
        # we use (l+(r-l)) instead of (l+r) because, if l and r are very large numbers, 
        #it might be a case that the addition of both of them results into a value that is beyond the range of python's limit to store.
        
        mid = start + (end - start) // 2

        if arr[mid] > target:
            end = mid-1

        elif arr[mid] < target:
            start = mid+1

        # target found
        else:
            return mid

    return -1

arr = [-18,-12,-4,0,2,3,4,15,16,18,22,45,89]
target = 4566
print(binary_search(arr,target))
