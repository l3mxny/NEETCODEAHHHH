class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        path = set()
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course,prereq in prerequisites:
            adj[course].append(prereq)
        res = []
        def dfs(course):
            if course in path:
                return False
            if course in visit:
                return True
            path.add(course)
            for prerequisite in adj[course]:
                if dfs(prerequisite) == False:
                    return False
            path.remove(course)
            visit.add(course)
            res.append(course)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
            
        