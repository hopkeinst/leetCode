class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x*(-1)
            strInt = str(x)
            strInt = strInt[::-1]
            y = (int(strInt))*(-1)
        else:
            strInt = str(x)
            strInt = strInt[::-1]
            y = int(strInt)
        minimo = (2**31)*(-1)
        maximo = (2**31)
        if (y < minimo) or (y > maximo):
            y = 0
        return y