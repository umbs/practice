class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 = not yet visited
        # -1 = currently being visited
        # 1 = already visited
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        for i in range(numCourses):
            if self.dfs(graph, visited, i) is False:
                return False
        
        return True
    
    def dfs(self, graph, visited, i):
        
        # Loop is found
        if visited[i] == -1:
            return False
        
        # Already examined this node
        if visited[i] == 1:
            return True
        
        visited[i] = -1
        for neigh in graph[i]:
            if self.dfs(graph, visited, neigh) is False:
                return False

        visited[i] = 1
        return True
