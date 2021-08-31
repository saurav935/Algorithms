

def order_agnostic_binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    is_ascending = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid

        if is_ascending:
            if arr[mid] > target:
                end = mid-1
            else:
                start = mid+1

        else:
            if arr[mid] < target:
                end = mid-1
            else:
                start = mid+1

    return -1

arr = [89, 45, 22, 18, 16, 15, 4, 3, 2, 0, -4, -12, -18]
target = 89
print(order_agnostic_binary_search(arr,target))

