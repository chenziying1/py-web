class Solution:
    def isPalindrome(self, x: int) -> bool:
        target = str(x)
        n = len(target)
        for i in range(n):
            if target[i] == target[n-i-1]:
                continue
            else:
                return False
        return True
