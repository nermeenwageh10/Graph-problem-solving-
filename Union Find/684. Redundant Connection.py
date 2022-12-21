class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d={ i:[] for i in range (1,len(edges)+1)}
        
        for n1,n2 in edges:
            d[n1].append(n2)
        
       