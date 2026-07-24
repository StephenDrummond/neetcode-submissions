class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if prereqs[crs] == []:
                return True
            
            seen.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            prereqs[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


