class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_freq = Counter(s)
        T_freq = Counter(t)
        if (S_freq == T_freq): return True
        return False
        