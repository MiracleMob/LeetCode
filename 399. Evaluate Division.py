class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = dict()
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        def dfs(s, t):
            if s not in graph or t not in graph:
                return -1
            if s == t:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        ans = []
        for (s, t) in queries:
            visited = set()
            ans.append(dfs(s, t))
        return ans

