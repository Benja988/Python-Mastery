def two_sum(arr, target):
    hashmap = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
        
        
def two_sum(nums, target):
    dict = {} # {num: index}
    for i, num in enumerate(nums): # [0,1,2,3,4,5]
        diff = target - num
        if diff in dict:
            return [dict[diff], i]
        dict[num] = i
        
        

