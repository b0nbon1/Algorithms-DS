class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of the strings are not equal, then they are not anagrams
        if len(s) != len(t):
            return False
        # Create a list of 26 elements, each element representing a character in the alphabet
        chrs = [0]*26
        # Iterate through the strings and increment the value of the character in the list
        for i in range(len(t)):
            # add the chars in s and subtract the chars in t from the list
            chrs[ord(s[i])-ord('a')] += 1
            chrs[ord(t[i])-ord('a')] -= 1
        
        # If the list contains any non-zero values, then the strings are not anagrams
        for n in chrs:
            if n != 0:
                return False
        
        return True

# Test cases
s = Solution()
print(s.isAnagram("anagram", "nagaram")) # True
print(s.isAnagram("rat", "car")) # False
print(s.isAnagram("a", "ab")) # False
print(s.isAnagram("a", "a")) # True