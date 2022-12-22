class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ## LOGIC ##
        #   1. make graph_ ==> { manager :  list_ of subordinates }
        
        def dfs( node, graph, totalTime ):
            
            self.res = max(self.res, totalTime)
            
            for sub in graph[node]:
                dfs( sub, graph, totalTime + informTime[node])
        
        
        if (n <= 1) : return 0
        
        import collections
        graph = collections.defaultdict(list)
        for i,m in enumerate(manager):
            if m == -1:
                continue
            graph[m].append(i)
        
        self.res = 0
        dfs( headID, graph, 0 )
        return self.res