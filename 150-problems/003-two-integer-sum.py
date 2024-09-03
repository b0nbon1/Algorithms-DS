class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store the difference between the target and the current number
        diffMap = {}
        # Iterate through the list of numbers
        for i, n in enumerate(nums):
            diff = target - n
            # If the difference is in the dictionary, then return the index of the difference and the current index
            if diff in diffMap:
                return [diffMap[diff], i]
            # Otherwise, add the current number to the dictionary
            diffMap[n] = i
        # If no solution is found, return [-1, -1]
        return [-1, -1]

# Test cases
s = Solution()
print(s.twoSum([2,7,11,15], 9)) # [0, 1]
print(s.twoSum([3,2,4], 6)) # [1, 2]
print(s.twoSum([3,3], 6)) # [0, 1]
print(s.twoSum([3,2,4], 5)) # [0, 1]
print(s.twoSum([3,2,4], 7)) # [0, 2]
print(s.twoSum([3,2,4], 8)) # [-1, -1]