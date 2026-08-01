class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(t))
        s2 = ''.join(sorted(s))

        if s1 == s2:
            return True
        else:
            return False