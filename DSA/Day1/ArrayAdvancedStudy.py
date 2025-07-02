# 1. Basic Array Operations => Iterate, update, insert and delete
arr = [1,2,3,4,5]
print(arr)
arr.append(4)
arr.remove(2)
arr[1] = 5
# for num in arr:
#     print(num)
    
    
# 2. Frequency Counting / Hash Map
from collections import Counter

arr = [2,3,2,3,4,6,7]
freq = Counter(arr)
for num in freq:
    if freq[num] == 1:
        print(num)


# 3. Two Pointers
arr = [1,2,3,4,6]
target = 7
l, r = 0, len(arr) - 1
while l < r:
    if arr[l] + arr[r] == target:
        print(arr[l], arr[r])
        break
    elif arr[l] + arr[r] < target:
        l += 1
    else:
        r -=1
        
        
# Sliding Window
arr = [1,4,2,10,2,3]
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)
print(max_sum)


# 4. Prefix Sum
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)
print(prefix[3] - prefix[1])


# In-place Algorithms
arr = [0,1,0,3,12,0,4]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
