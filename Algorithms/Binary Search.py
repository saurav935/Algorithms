

def binary_search(arr,target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        
        # find the middle element
        # we use (l+(r-l)) instead of (l+r) because, if l and r are very large numbers, 
        #it might be a case that the addition of both of them results into a value that is beyond the range of python's limit to store.
        
        mid = l + (r-l) // 2

        if arr[mid] > target:
            r = mid-1

        elif arr[mid] < target:
            l = mid+1

        # target found
        else:
            return mid

    return -1

arr = [-18,-12,-4,0,2,3,4,15,16,18,22,45,89]
target = 4566
print(binary_search(arr,target))
