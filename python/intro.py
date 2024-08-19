n, m = 0, 'abc'
print('n', n, m)

# Null
# null = None
# if n > 2:
#     n -= 1
# elif n == 2:
#     n *= 2
# else:
#     n += 2

# && = and, || = or
# if (n> 2 and n < 3):
#     n += 7

# for i in range(5):
#     print(i)

# reverse loop
# for i in range(5, -1, -1):
#     print(i)

# print(5/2)
# print(5//2)

# print(10 % 3)
# print(math.fmod(-10, 3))

# max and Min
# maxVal = float("inf")
# minVal = float("-inf")

# arr = [1,2,3]
# print(arr)

# # Can be used as stack 
# arr.append(4)
# arr.append(5)
# print(arr)

# # pop
# arr.pop()
# print(arr)

# # insert
# arr.insert(1,7)
# print(arr)

# arr[0] = 8
# arr[3] = 9
# print(arr)

# n=5
# arr = [0]*n
# print(arr)

# print(arr[-1]) # last value

# Sublists (aka slicing)
# arr = [1, 2, 3, 4]
# print(arr[1:3])

# # Similar to for-loop ranges, last index is non-inclusive
# print(arr[0:4])

# # But no out of bounds error
# print(arr[0:10])

# # Unpacking
# a, b, c = [1, 2, 3]
# print(a, b, c)

# Loop through arrays
# nums = [1, 2, 3]

# # Using index
# for i in range(len(nums)):
#     print(nums[i])

# # Without index
# for n in nums:
#     print(n)

# # With index and value
# for i, n in enumerate(nums):
#     print(i, n)

# Loop through multiple arrays simultaneously with unpacking
# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)

# # Reverse
# nums = [1, 2, 3]
# nums.reverse()
# print(nums)

# # Custom sort (by length of string)
# arr.sort(key=lambda x: len(x))
# print(arr)

# # List comprehension
# arr = [i for i in range(5)]
# print(arr)

# # 2-D lists
# arr = [[0] * 4 for i in range(4)]
# print(arr)
# print(arr[0][0], arr[3][3])


# # Strings are similar to arrays
# s = "abc"
# print(s[0:2])

# # But they are immutable
# # s[0] = "A"

# # So this creates a new string
# s += "def"
# print(s)

# # Valid numeric strings can be converted
# print(int("123") + int("123"))

# # And numbers can be converted to strings
# print(str(123) + str(123))

# # In rare cases you may need the ASCII value of a char
# print(ord("a"))
# print(ord("b"))

# # Combine a list of strings (with an empty string delimitor)
# strings = ["ab", "cd", "ef"]
# print("".join(strings))

# Queues (double ended queue)
# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# print(queue)

# queue.popleft()
# print(queue)

# queue.appendleft(1)
# print(queue)

# queue.pop()
# print(queue)
