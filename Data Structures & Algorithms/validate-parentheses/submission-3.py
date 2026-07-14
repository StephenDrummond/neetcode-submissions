class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        op = ('(','{','[')
        cl = (')','}',']')

        for c in s:
            if c in op:
                q.append(c)
            else:
                if not q or cl.index(c) != op.index(q.pop()):
                    return False
        
        return True if not q else False