def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countT == countS

def isAnagram1(s,t):
    if len(s) != len(t):
        return False
    
    freq = [0]*26
    for i in range(len(s)):
        freq[ord(s[i])- ord('a')] += 1
        freq[ord(t[i])- ord('a')] -= 1
    
    for f in freq:
        if f != 0:
            return False
    
    return True
    

print(isAnagram1("abde", "aedb"))
