def quicksort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo >= hi: return arr
    
    # Partition the array and recursively sort the left and right halves
    pivot = partition(arr, lo, hi)
    quicksort(arr, lo, pivot-1)
    quicksort(arr, pivot+1, hi)
    
    return arr

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    
    # Partition the array into two halves
    for j in range(lo, hi):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    
    # Swap the pivot with the element at index i (the first element in the right half)
    swap(arr, i, hi)
    return i

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
