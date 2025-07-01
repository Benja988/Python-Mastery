arr = [1,2,3,4,5,6,7]

# 1. Traversal
for i in range(len(arr)):
    print(arr[i])
    
# 2. Insert at the end
arr.append(6)

# 3. Insert at index
arr.insert(2, 56)

# 4. Delete at Index
arr.pop(2)

# 5. Delete by value
arr.remove(5)

# 6. Search
if 3 in arr:
    print("found")

# 7. Reverse an array
arr.reverse() # OR arr [::-1]

print(arr)