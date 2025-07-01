def two_sum(arr, target):
    hashmap = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i