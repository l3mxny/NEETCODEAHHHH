#mysolution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        result = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) +1
            max_freq = max(count.values())
            #invalid window, move left forward
            if (right-left+1) - max_freq > k :
                count[s[left]] = count.get(s[left],0) - 1
                left += 1
            result = max(right - left + 1, result)
        
        return result