# search array from left to right
def linear_search(arr: list, num: int):
    for index in range(0, len(arr)):
        if arr[index] == num:
            return index
    return -1

print(linear_search([1,44,22,1,3,55,245,73,11], 11))