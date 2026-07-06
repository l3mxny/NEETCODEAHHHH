#dfs
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {}
        for i in range(n):
            adj[i] = []
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node):
            #node visited
            visit.add(node)
            for neighbor in adj[node]:
                #component neighbor still has more nodes keep exploring
                if neighbor not in visit:
                    dfs(neighbor)
        counter = 0   
        for i in range(n):
            #new component
            if i not in visit:
                counter += 1
                dfs(i)
        return counter