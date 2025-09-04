# Variables, Data Types, and Operators
x = 5
y = 3
# print(x + y)

msg = "Hello Developer"
# print(msg[0])
# print(msg[0:5])
# print(msg[::-1])

is_dev = True


# Strings
s1 = "hello"
s2 = "Developer"
s3 = """multi-line strings"""

# Indexing and slicing
s1[0]
s1[-1]
s1[0:5]
s1[::-1]  # Reverse

# Case Conversion
s1.upper()
s2.lower()
s3.title()
s1.strip()


# Lists
l1 = [1, 2, 3, 4, 5]
l2 = ["a", "b", "c", "d", "e"]
l3 = [1, "a", 2, "b", 3, "c", 4, "d", 5, "e"]

# Indexing and Slicing
l1[0] 
l1[-1]
l1[0:3]
l1[::-1]

# Lists Methods
l1.append(6)
l1.insert(0, 0)
l1.remove(2)
l1.pop()
l1.clear()
l1.copy()

# Tuples
t1 = (1, 2, 3, 4, 5)
t2 = ("a", "b", "c", "d", "e")
t3 = (1, "a", 2, "b", 3, "c", 4, "d", 5, "e")

# Tuples Methods
t1.count(2)
t1.index(3)


nums = [10, 20, 30, 40, 50]
for i, v in enumerate(nums): # for i, v in nums:
    print(i, v)
    
for i in range(5):
    print(i)
    
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)
    
x=3