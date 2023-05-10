class Solution:
    def romanToInt(self, s: str) -> int:
        integer = []
        for roman in s:
            match roman:
                case 'I':
                    integer.append(1)
                case 'V':
                    integer.append(5)
                case 'X':
                    integer.append(10)
                case 'L':
                    integer.append(50)
                case 'C':
                    integer.append(100)
                case 'D':
                    integer.append(500)
                case 'M':
                    integer.append(1000)
        
        result = 0

        for i in range(len(integer) - 1):
            if integer[i] >= integer[i+1]:
                result += integer[i]
            else:
                result -= integer[i]

        return result + integer[-1]
