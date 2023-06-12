# quick sort

def quick_sort(x, start, end):
    if start >= end:
        return

    pivot = start
    i = pivot + 1
    j = end

    while i <= j:
        while i <= end and x[pivot] >= x[i]:
            i += 1
        while j > pivot and x[pivot] <= x[j]:
            j -= 1
        # i 그리고 j 가 서로 엇갈리지 않은 경우
        if i <= j:
            x[i], x[j] = x[j], x[i]
        # i 그리고 j 가 서로 엇갈린 경우
        else:
            x[pivot], x[j] = x[j], x[pivot]

    quick_sort(x, start, j - 1)
    quick_sort(x, j + 1, end)


numbers = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(numbers)
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
