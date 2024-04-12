# search sorted array for a number

def binary_search(arr: list, num: int) -> int:
    l = 0 
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == num:
            return mid
        elif num >= arr[mid]:
            l = mid + 1
        else: r = mid - 1
    return

print(binary_search([1,2,4,5,6,8,9,0], 14))