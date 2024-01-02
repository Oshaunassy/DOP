def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = bubble_sort(unsorted_list.copy())
print("Sorted list:", sorted_list)

element_to_search = 6
result = binary_search(sorted_list, element_to_search)

if result != -1:
    print(f"Element {element_to_search} found by index {result}.")
else:
    print(f"Element {element_to_search} not found.")