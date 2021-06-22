class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reverse_str = x_str[::-1]
        if x_str == reverse_str:
            return True
        else:
            return False