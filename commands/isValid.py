class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        brackets = {"(" : ")", "[" : "]", "{" : "}"}
        queue = []
        for char in s:
            if char in brackets.keys():
                queue.append(brackets.get(char))
            else:
                if len(queue) > 0:
                    if char != queue.pop(-1):
                        return False
                else:
                    return False
        if len(queue) > 0:
            return False
        return True