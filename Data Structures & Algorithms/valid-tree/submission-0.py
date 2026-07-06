class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        #breaks tree def 
        if n-1 != len(edges):
            return False
        adj = {}
        for i in range(n):
            adj[i] = []
        for a,b in edges:
            adj[a].append(b)
        #undirected
        for a,b in edges:
            adj[b].append(a)
        #track prev (undirected f)
        def dfs(nodes,prev):
            visit.add(nodes)
            for neighbor in adj[nodes]:
                if neighbor == prev: 
                    continue
                #must be a cycle (after prev check)
                if neighbor in visit:
                    return False
                if not dfs(neighbor,nodes):
                    return False
            return True
        prev = None
        ans = dfs(0,None)
        if ans and len(visit) == n:
            return True
        return False

        