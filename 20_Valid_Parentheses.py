class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            # Try coz index error will mean terms are not served
            try:
                # Creates a stack of open parenthesis
                if char == '(' or char == '{' or char == '[':
                    stack.append(char)
                # Checks if last parenthesis in stack match next one
                else:
                    match char:
                        case ')':
                            if stack[-1] == '(':
                                del stack[-1]
                            else:
                                return False
                        case ']':
                            if stack[-1] == '[':
                                del stack[-1]
                            else:
                                return False
                        case '}':
                            if stack[-1] == '{':
                                del stack[-1]
                            else:
                                return False
            except IndexError:
                return False
        
        if not stack:
            return True
