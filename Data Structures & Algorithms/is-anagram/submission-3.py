class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = Counter(s)
        for char in t:
            if char in frequency: 
                frequency[char] -= 1
                if frequency[char] == 0:
                    frequency.pop(char)
            else: return False
        if (len(frequency) == 0): return True
        return False
        