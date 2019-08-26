class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        # 拓扑排序 BFS 图中不存在环
        # 入度表
        indegree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        for nt, pre in prerequisites:
            indegree[nt] += 1
            adjacency[pre].append(nt)

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for nt in adjacency[pre]:
                indegree[nt] -= 1
                if indegree[nt] == 0:
                    queue.append(nt)

        return numCourses == 0

