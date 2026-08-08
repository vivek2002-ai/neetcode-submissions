class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = dict({'(':')','{':'}','[':']'})
        for bracket in s:
            if stack == []:
                stack.append(bracket)
                continue
            last_bracket = stack[-1]
            if bracket == matching_bracket.get(last_bracket,''):
                stack.pop()
            else:
                stack.append(bracket)
        return True if len(stack)==0 else False
        