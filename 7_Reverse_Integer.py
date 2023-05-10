class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)

        if x[0] == '-':
            x = x[1:] + '-'
        x = int(x[::-1])

        if x > 2147483648 or x < -2147483648:
            x = 0

        return x
