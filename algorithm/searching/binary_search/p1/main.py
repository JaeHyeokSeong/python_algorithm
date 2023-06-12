# binary search

def binary_search(x, start: int, end: int, find) -> bool:
    x = sorted(x)
    i = start
    j = end

    while i <= j:
        mid = (i + j) // 2
        if x[mid] == find:
            return True
        elif x[mid] < find:
            i = mid + 1
        else:
            j = mid - 1

    return False


numbers = [3, 1, 2, 5, 6, 4, 8, 7, 9, 10]
find = 10
result = binary_search(numbers, 0, len(numbers) - 1, find)
print(result)
