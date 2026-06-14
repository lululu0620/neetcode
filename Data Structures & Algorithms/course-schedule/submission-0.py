class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses
        visited = [False] * numCourses
        graph = defaultdict(list)
        for prev, curr in prerequisites:
            degrees[curr] += 1
            graph[prev].append(curr)
        queue = deque()
        for i, degree in enumerate(degrees):
            if degree == 0:
                queue.append(i)
        if not queue:
            return False
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                visited[curr] = True
                for nxt in graph[curr]:
                    if visited[nxt]:
                        continue
                    degrees[nxt] -= 1
                    if degrees[nxt] == 0:
                        queue.append(nxt)
        for degree in degrees:
            if degree > 0:
                return False
        return True
        