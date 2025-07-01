def missing_number(arr):
    n = len(arr)
    expected = n * (n + 1) // 2
    return expected - sum(arr)


# Check is array is sorted and rotated

def is_sorted_and_rotated(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
    return count <= 1