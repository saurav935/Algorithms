

def order_agnostic_binary_search(arr,target):
    l = 0
    r = len(arr) - 1
    is_ascending = arr[l] < arr[r]

    while l <= r:
        mid = l + (r-l) // 2

        if arr[mid] == target:
            return mid

        if is_ascending:
            if arr[mid] > target:
                r = mid-1
            else:
                l = mid+1

        else:
            if arr[mid] < target:
                r = mid-1
            else:
                l = mid+1

    return -1

arr = [89, 45, 22, 18, 16, 15, 4, 3, 2, 0, -4, -12, -18]
target = 89
print(order_agnostic_binary_search(arr,target))

