def containsDuplicate(nums):
    s = set()
    for n in nums:
        if n in s:
            return True
        s.add(n)
    
    return False
