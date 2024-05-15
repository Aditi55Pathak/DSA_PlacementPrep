# Chocolate distribution problem

def min_diff_chocolates(arr, m):
    if m > len(arr):
        return -1

    arr.sort()

    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
result = min_diff_chocolates(arr, m)
print("Minimum Difference is", result)