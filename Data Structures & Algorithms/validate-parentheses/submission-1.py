class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in "({[":
                stack.append(char)

            if char in ")}]":
                if not stack:
                    return False
                
                current = stack.pop()

                if reference[current] != char:
                    return False

        return not stack
