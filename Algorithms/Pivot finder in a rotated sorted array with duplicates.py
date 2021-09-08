
def pivot_finder(self ,arr):
    l = 0
    r = len(arr ) -1

    while l < r:
        mid = l + ( r -l) // 2

        if mid < r and arr[mid] > arr[mi d +1]:
            return mid

        if mid > l and arr[mid] < arr[mi d -1]:
            return mi d -1

        # For duplicates
        if arr[mid] == arr[l] and arr[mid] == arr[r]:
            if arr[l] > arr[ l +1]:
                return l
            else:
                l += 1

            if arr[r] < arr[ r -1]:
                return r- 1
            else:
                r -= 1


        elif arr[mid] > arr[l] or arr[mid] == arr[l] and arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid - 1

    return -1

