def bubble_sort(arr: list) -> list:
    for j in range(len(arr) - 1):
        swapped = False
        for i in range((len(arr) - 1 - j)):
            print(arr)
            num = arr[i]
            if num > arr[i+1]:
                arr[i] = arr[i+1]
                arr[i+1] = num
                swapped = True
        if not swapped:
            break     
    return arr


