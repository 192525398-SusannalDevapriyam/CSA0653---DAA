def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, iterations

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, iterations


arr = list(range(1, 65))

target = 60

position, iterations = binary_search(arr, target)

print("Dataset Size:", len(arr))
print("Target:", target)
print("Position:", position)
print("Iterations:", iterations)

input("\n\npress enter to exit...")