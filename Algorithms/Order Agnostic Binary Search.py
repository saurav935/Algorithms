

def order_agnostic_binary_search(arr,target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        # find the middle element
        # we use (l+(r-l)) instead of (l+r) because, if l and r are very large numbers, it might be a case that the addition of both of them results into a value that is beyond the range of python's limit to store.
        mid = l + (r-l) // 2

        if arr[mid] > target:
            l = mid+1

        elif arr[mid] < target:
            r = mid-1

        # target found
        else:
            return mid

    return -1

arr = [89, 45, 22, 18, 16, 15, 4, 3, 2, 0, -4, -12, -18]
target = 120
print(order_agnostic_binary_search(arr,target))

