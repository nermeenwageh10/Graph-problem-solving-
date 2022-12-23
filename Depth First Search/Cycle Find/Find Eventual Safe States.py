class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        T = set([n for n in range(N) if not graph[n]])
        V = set()
        def dfs(node,visited):
            if node in T:
                return True
            if node in V or node in visited:
                return False
            visited.append(node)
            for n in graph[node]:
                if not dfs(n,visited):
                    V.add(node)
                    V.add(n)
                    return False
                else:
                    T.add(n)
            T.add(node)
            return True
        res = [n for n in range(N) if dfs(n,[])]
        return res