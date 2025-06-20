def lengthOfLongestSubstring( s: str) -> int:
    s = set(s)
    left = 0
    maxlen = 0
        
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        maxlen = max(maxlen , right-left +1)
            
    return maxlen
                

print(lengthOfLongestSubstring("aacbabcbcc"))    
