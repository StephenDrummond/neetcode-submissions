class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereqs = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        seen = set()
        seenall = set()
        flag = True

        def dfs(crs):
            if crs in seen:
                return False
            if prereqs[crs] == []:
                return True
            
            seen.add(crs)

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
                if pre not in seenall:
                    seenall.add(pre)
                    res.append(pre)
            seen.remove(crs)
            prereqs[crs] = []
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        courses = set([x for x in range(numCourses)])
        courses = courses ^ set(res)
        res.extend(courses)
        return res