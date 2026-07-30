class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If char was seen and its last index is inside the current window
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            # Record current char position and update max length
            seen[char] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len
