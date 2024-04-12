# sort array using a pivot
def quicksort(arr: list, start: int, end: int)-> None:
    if end <= start: return # base case
    pivot = partition(arr, start, end)
    quicksort(arr, start, pivot - 1)
    quicksort(arr, pivot + 1, end)


def partition(arr: list, start: int, end: int)-> int:
    # set pivot to end of partition
    pivot_value = arr[end]
    # set pointers to start of partition and index before start
    i = start - 1
    j = start
    # compare all values in partition with the pivot value
    while j < end:
        # if val < pivot value, swap values at pointers
        if arr[j] < pivot_value:
            i+=1
            arr[i], arr[j] = arr[j], arr[i] 

        j+=1
    # increment i and swap its value with pivot value
    i+=1 
    arr[i], arr[end] = arr[end], arr[i]

    return i


array = [1,44,3,2,66,42,63,84,12,3,7]
quicksort(array, 0, len(array) - 1)
print(array)