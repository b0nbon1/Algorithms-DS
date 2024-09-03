from collections import defaultdict

# space complexity: O(n)
# time complexity: O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # count the frequency of each number
        count = defaultdict(int)
        # count the frequency of each number
        for n in nums:
            count[n] += 1
    
        # create a list of list to store the number with the same frequency(known as buckets)
        freq = [[] for i in range(len(nums)+1)]
        # store the number with the same frequency in the same index(bucket)
        for n,v in count.items():
            freq[v].append(n)
        
        res = []
        # iterate the bucket from the end to the start, to get the number with the highest frequency
        for i in range(len(freq)-1, 0, -1):
            # if the bucket is not empty, append the number to the result list
            for n in freq[i]:
                res.append(n)
                # if the result list has k elements, return the result list
                if len(res) == k:
                    return res
        
        return res

# test
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k)) # [1,2]
