from collections import defaultdict

# space complexity: O(n*26) = O(n)
# time complexity: O(n*m) because we are iterating through the list of strings and the string itself
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a dictionary to store the groups of anagrams
        group = defaultdict(list)
        # Iterate through the list of strings
        for s in strs:
            # Create a list of 26 elements, each element representing a character in the alphabet
            chrs = [0]*26
            # Iterate through the string and increment the value of the character in the list
            for c in s:
                chrs[ord(c)-ord('a')] += 1
            
            # Add the string to the group of anagrams
            group[tuple(chrs)].append(s)
        
        # Return the values of the dictionary
        return list(group.values())

# Test cases
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
