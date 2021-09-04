
def pivot_finder(self, arr):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if mid < r and arr[mid] > arr[mid + 1]:
            return mid
        if mid > l and arr[mid] < arr[mid - 1]:
            return mid - 1
        if arr[mid] <= arr[l]:
            r = mid - 1
        else:
            l = mid + 1

    return -1