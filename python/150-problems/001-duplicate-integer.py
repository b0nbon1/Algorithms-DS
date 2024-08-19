# https://neetcode.io/problems/duplicate-integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Create a set to be used to check if the number is duplicate or not.
# loop through nums while checking if number already exists in out set if not add if exists return True the array contains a duplicate
# Otherwise return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()
        for n in nums:
            if n not in dupSet:
                dupSet.add(n)
            else:
                return True
        return False
