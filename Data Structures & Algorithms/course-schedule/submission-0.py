class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        path = set()
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course,prereq in prerequisites:
            adj[course].append(prereq)
        def dfs(crs):
        #cycle
            if node in path:
                return False
            #safe
            if node in visit:
                return True
            path.add(node)
            for neighbor in adj[node]:
                #cycle in neighbor
                if dfs(neighbor) == False:
                    return False
            #no cycle, add to safe visit
            path.remove(node)
            visit.add(node)
            return True
        for course in range(numCourses):
            if dfs(course) is False:
                return False
        return True
        